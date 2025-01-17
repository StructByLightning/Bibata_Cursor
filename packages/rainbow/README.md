<!-- Branding -->

<p align="center">
  <img src="./src/svgs/branding/logo.svg" width="15%">
</p>

<p align="center">
  <b>Semi-Animated bibata cursors with rainbow colors</b> 🌈
</p>

<!-- Badges -->

<p align="center">

  <!-- First Row -->

  <a href="https://github.com/ful1e5/Bibata_Cursor/actions?query=workflow%3Abibata-rainbow-ci">
    <img alt="GitHub Action Build" src="https://github.com/ful1e5/Bibata_Cursor/workflows/bibata-rainbow-ci/badge.svg" />
  </a>
  
  <a href="https://www.codefactor.io/repository/github/ful1e5/bibata_cursor">
    <img src="https://www.codefactor.io/repository/github/ful1e5/bibata_cursor/badge" alt="CodeFactor" />
  </a>
  
  <a href="https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html">
    <img alt="npm type definitions" src="https://img.shields.io/npm/types/typescript">
  </a>

  <!-- Second Row -->

  <br />

  <a href="https://aur.archlinux.org/packages/bibata-rainbow-cursor-theme" >
    <img alt="AUR version" src="https://img.shields.io/aur/version/bibata-rainbow-cursor-theme">
  </a>

  <a href="https://github.com/ful1e5/clickgen">
    <img alt="Clickgen" src="https://img.shields.io/badge/theme%20builder-clickgen-FD0542" />
  </a>
  
  <a href="https://www.pling.com/p/1197198/#files-panel">
    <img alt="License" src="https://img.shields.io/badge/-Linux-grey?logo=linux" />
  </a>

  <!-- <a href="https://www.pling.com/p/1197198/#files-panel">
    <img alt="License" src="https://img.shields.io/badge/-Windows-blue?logo=windows" />
  </a> -->

  <!-- Third Row -->

  <br />
  <a href="https://github.com/ful1e5">
    <img alt="Made By Kaiz"  src="https://kaiz.vercel.app/api/badge" width="133" />
  </a>

</p>

---


## Quick install

<p align="center">
  <a href="https://www.pling.com/p/1445634/" >
    <img title="Bibata Rainbow Pling Store" width="40%" src="https://imgur.com/VxSgrWw.png">
  </a>
</p>

## Cursor Sizes

<kbd>22</kbd>
<kbd>24</kbd>
<kbd>28</kbd>
<kbd>32</kbd>
<kbd>40</kbd>
<kbd>48</kbd>
<kbd>56</kbd>
<kbd>64</kbd>
<kbd>72</kbd>
<kbd>80</kbd>
<kbd>88</kbd>
<kbd>96</kbd>

## Preview 

<p align="center">
  <img alt="Bibata Rainbow" src="./src/svgs/branding/preview.svg" width="90%">
  </br>
  <sub>Bibata Rainbow</sub>
</p>

## Packages 📦

> **📝Note**: If you're having trouble with the packages please submit a request to the package maintainer before creating an issue.

### Arch Linux/Manjaro

Arch Linux/Manjaro users can install from the [AUR](https://aur.archlinux.org/packages/bibata-rainbow-cursor-theme) currently maintained by [_@yochananmarqos_](https://aur.archlinux.org/packages/?K=yochananmarqos&SeB=m). Can be installed via Pamac (preinstalled in Manjaro), Yay or any other [AUR helper](https://wiki.archlinux.org/index.php/AUR_helpers).

Pamac command:

```bash
pamac build bibata-rainbow-cursor-theme
```

Yay command:

```bash
yay -S bibata-rainbow-cursor-theme
```

## Manual Install

Latest `Stable` & `Development` releases can be downloaded from [Here](https://github.com/ful1e5/Bibata_Cursor/releases)

#### Linux/X11

```bash
# extract `Bibata-Rainbow.tar.gz`
tar -xvf Bibata-Modern-Rainbow.tar.gz
tar -xvf Bibata-Original-Rainbow.tar.gz

# For local users
mv Bibata-*-Rainbow ~/.icons/

# For all users
sudo mv Bibata-*-Rainbow /usr/share/icons/
```
## Build From Scratch

**[dependencies](../../README.md#dependencies)** same as **bibata**.

### ⚡ Auto Build (using GitHub Actions)

GitHub Actions is automatically runs on every `push`(on **main** & **dev** branch) and `pull request`(on **main** branch), You found theme resources in `artifact` section of **bibata-rainbow-ci**. GitHub **Actions** available inside [.github/workflows](https://github.com/ful1e5/Bibata_Cursor/tree/main/.github/workflows) directory.

### Manual Build

> Make sure your [python environment](../../README.md#setup-python-environment) setup and `virtualenv` is **active**.
> Run these 👇 commands in **root** of project.

#### Install Node/PyPi Packages

```bash
yarn install                                         # Install all Node Packages
yarn py_install                                      # Install all PyPi Packages with Bibata builder
```

#### Build `Bibata-Rainbow`

```bash
yarn render:bibata-rainbow                           # Render Bibata-Rainbow Bitmaps

# Build cursors packages
yarn build                                           # Build Windows & X11 packages
# OR
yarn build:x11                                       # Build only X11 packages
# OR
yarn build:win                                       # Build only Windows cursors
```
After build `bitmaps` and `themes` directory are generated at project **root**.

### Install Build Theme

All builded cursor themes are available inside `themes` directory.

#### Linux

```bash
cd ./themes

# installing Theme to local user(recommend)
rm -rf ~/.icons/Bibata-*-Rainbow && cp -r Bibata-*-Rainbow ~/.icons/
```