# The requirements.sh is an advanced mechanism an should rarely be needed.
# Be aware that it won't run with root permissions and 'sudo' won't work
# in most cases.

#detect distribution using lsb_release (may be replaced parsing /etc/*release)
dist=$(lsb_release -d |awk '{print$2}')

#setting dependencies and package manager in relation to the distribution
if [ "$dist"  == "Arch"  ]; then
    pm="pacman -S"
elif [ "$dist" ==  "Ubuntu" ] || [ "$dist" == "KDE" ] || [ "$dist" == "Debian" ]; then
    pm="apt install"
fi
dependencies=( espeak )


# installing dependencies
for dep in "${dependencies[@]}"
do
    sudo $pm $dep
done
