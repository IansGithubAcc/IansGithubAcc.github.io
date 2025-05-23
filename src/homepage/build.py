from sphinx.cmd.build import main

if __name__ == "__main__":
    main(('-b', 'html', 'sphinx/source', 'docs'))