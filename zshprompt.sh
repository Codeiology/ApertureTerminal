# Define the colors for your prompt
GREEN='%F{green}'
YELLOW='%F{yellow}'
BLUE='%F{blue}'
RED='%F{red}'
PURPLE='%F{magenta}'
CYAN='%F{cyan}'
GRAY='%F{gray}'
WHITE='%F{white}'
NO_COLOR='%f'

# Enable prompt substitution
setopt PROMPT_SUBST

# Set your custom prompt
PS1="${GREEN}ne0${NO_COLOR}@${BLUE}aperturescience ${YELLOW}%~${CYAN}\$(parse_git_branch)${NO_COLOR} >> "

# Define a function to show the git branch name in the prompt
function parse_git_branch {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e "s/* ${GRAY}\\(.*\\)/${PURPLE}(\\1)${NO_COLOR}/"
}