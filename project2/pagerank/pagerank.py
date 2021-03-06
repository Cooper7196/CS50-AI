import copy
import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    amountOfPages = len(corpus.keys())
    linkedPages = corpus[page]

    if len(linkedPages) == 0:
        linkedPages = corpus.keys()
    output = {page: 0 for page in corpus.keys()}

    for page in linkedPages:
        output[page] = damping_factor / len(linkedPages)

    for page in output.keys():
        output[page] += (1 - damping_factor) / amountOfPages

    return output


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    output = {page: 0 for page in corpus.keys()}
    page = random.choice(list(corpus.keys()))
    output[page] += 1
    for i in range(n):
        currentProbabilities = transition_model(corpus, page, damping_factor)
        page = random.choices(
            list(currentProbabilities.keys()),
            list(currentProbabilities.values()))[0]
        output[page] += 1
    output = {k: v / n for k, v in output.items()}
    return output


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    totalPages = len(corpus.keys())
    oldOutput = {page: 0 for page in corpus.keys()}
    output = {page: 1 / totalPages for page in corpus.keys()}
    totalIterations = 0
    while True:
        newOutputs = {}
        for page in corpus.keys():
            minimumProbability = ((1 - damping_factor) / totalPages)
            summationPobability = 0
            for linkingPage in corpus.keys():
                linkedPages = list(corpus[linkingPage])
                if len(linkedPages) == 0:
                    linkedPages = list(corpus.keys())
                if page in linkedPages:
                    summationPobability += output[linkingPage] / \
                        len(linkedPages)
            newOutputs[page] = minimumProbability + \
                (damping_factor * summationPobability)

        for k, v in newOutputs.items():
            output[k] = v
        totalIterations += 1
        isSettled = True
        differences = {}
        for k, v in output.items():
            differences[k] = abs(oldOutput[k] - v)
            if abs(oldOutput[k] - v) > 0.001:
                isSettled = False
        if isSettled:
            return output
        oldOutput = copy.deepcopy(output)


if __name__ == "__main__":
    main()
