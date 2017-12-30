
git branch svgs

yes | python -m readme2tex --usepackage "tikz" --usepackage "xcolor" --output README.md --branch svgs INPUT.md --add-git-hook

chmod +x .git/hooks/post-commit
