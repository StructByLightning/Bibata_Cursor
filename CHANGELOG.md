# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

# Tags

- Normal tagging for **Bibata** (v1.0.0)
- Tag with `br` postfix in **Bibata Rainbow** (v1.0.0.br)

## [unreleased]

### Added
- new **[copr](https://copr.fedorainfracloud.org/coprs/peterwu/rendezvous/package/bibata-cursor-themes/)** package by @peterwu

## [Bibata Rainbow v1.0.0] - 17 Nov 2020

### Added

- **Bibata Rainbow** (semi-animated) cursors. **#55**
- **Bibata Rainbow** workflow file added `bibata-rainbow-ci.yml`
- **semi-animated** cursors `.svg` parsing support in `bibata-core`
- `PLING.bbcode` for Bibata Rainbow
- Tagging guid in [CHANGELOG.md](./CHANGELOG.md#tags)
- Bibata Rainbow's **branding** assets in `packages/rainbow/src/svgs/branding`

### Changed

- `build` workflow changed to `bibata-ci`
- **Bibata** workflow file names changed to `bibata-ci.yml` & `bibata-pr.yml`
- Optimize **BitmapsGenerator** browser.

## [Bibata v1.0.3] - 10 Nov 2020

### Added

- Case insensitive `colors key` replace in **bibata-core**
- **Alternate.cur** added in Windows package
- `minimumFrames` frames handler added for animated cursors in **bibata-core**

### Changed

- Files download reference change to [pling.com](https://www.pling.com/p/1197198/) in `PLING.bbcode`
- Scripts in `package.json`
- Change reference of **Alternate.cur** to `right_ptr`
- fixed #82 improvement to X-cursor (feature request)
- fixed #81 Corner resize cursors are not coloured (bug)

## [Bibata v1.0.2] - 30 Oct 2020

### Added

- Separate **GitHib Action** workflow for **pull-request**
- **pkg_info.py** inside `builder` module
- `builder` module docs

### Changed

- Windows Resize cursors wrong implementation fixed **#76** [Reopen]
- **Rich Black** color in `watch: background` (Bibata Amber) **#78**
- PyPi Requirements provided inside `setup.py`
- locked clickgen to **1.1.7**
- Package information provider module changed to `builder/pkg_info.py`

## [Bibata v1.0.1] - 8 Oct 2020

### Added

- **[builder](./builder/)** python package
- Build only **x11** cursors by passing `--x11` flag in `build.py`
- Build only **win** cursors by passing `--win` flag in `build.py`
- Bump up **clickgen** version to **1.1.7** (KDE cursors fix patch)
- `22px` size added (suggestion by **@gotroot** from pling.com)

### Changed

- Browser args changed in `bibata-core` **BitmapGenerator**
- **yarn** scripts updated
- **yarn-packages** description updated
- **Installation** docs updated in [README.md](./README.md) & [PLING.bbcode](./PLING.bbcode)
- remove additional comments in **[PULL_REQUEST_TEMPLATE.md](https://github.com/ful1e5/Bibata_Cursor/commit/085221352038a199aae99f828d64b2ae91ace493)**
- #76 Wrong implementation resize cursors **[closed]**
- #74 `Pillow` pip requirements checking in installation of **clickgen**

## [Bibata v1.0.0] - 3 Oct 2020

### Changed

- `main` as **default** branch
- Package **size** reduced
- Build process with `python` & [**clickgen**](https://github.com/ful1e5/clickgen)
- Cursors Redesign => `all_scroll`, `pencil`, `wayland_cursor`, `xcursor` and all `pointer symbols`(with Bigger Symbols) cursors
- `Bibata Oil` is **end of life**
- Bitmaps Rendering with [**puppeteer**](https://github.com/puppeteer/puppeteer)
- Build Docs

### Added

- Bibata Original (Old Bibata)
- Windows Package with **Double Click** installation 😍
- Maintaining [CHANGELOG.md](./CHANGELOG.md)
- [CURSORS.md](./CURSORS.md) for all cursors information
- [PLING.bbcode](./PLING.bbcode) for pling.com Product page docs
- [GitHub Actions](https://github.com/ful1e5/Bibata_Cursor/actions) added
- New Build with **10x** faster rendering.
- Customizable Colors in **Bibata** Cursors.
- Auto framing in animated cursors with [**pixelmatch**](https://github.com/mapbox/pixelmatch)

## [Bibata v0.4.2] - 12 January 2020

### Changed

- same names in Oil and Classic [Fixed again]

## [Bibata v0.4.2.beta.1] - 22 December 2019

### Changed

- Bibata Logo resigned

## [Bibata v0.4.2.alpha.2] - 1 December 2019

### Added

- Fresh new Aminated cursors
- Missing KDE Cursors
- Added custom animation-delay tweak script

### Changed

- Glitch fixed in watch cursor(loading state)
- Bibata Amber Color changed to #FF8000
- Bibata Oil is inspired on **adwaita gtk** theme color #272728

## [Bibata v0.4.2.alpha.1] - 13 November 2019

### Added

- New build process using python
- Common .svg file for all cursor source(i.e. time saving for modification)
- Bibata Classic Flavor
- Available for Windows user

### Changed

- Color & Shadow changed for easy visibility
- Cursor's corner-shape changed
- Hot-spots changed

## [Bibata v.0.4.1] - 3 September 2018

### Changed

- Locations Fixed
- AUR added in README.md

## [Bibata v0.3.1] - 16 March 2018

### Changed

- Redesign Crosshair

## [Bibata v0.3] - 3 February 2018

### Added

- Initial release 🎊

[unreleased]: https://github.com/ful1e5/Bibata_Cursor/compare/v1.0.0.br...main
[bibata rainbow v1.0.0]: https://github.com/ful1e5/Bibata_Cursor/compare/v1.0.3...v1.0.0.br
[bibata v1.0.3]: https://github.com/ful1e5/Bibata_Cursor/compare/v1.0.2...v1.0.3
[bibata v1.0.2]: https://github.com/ful1e5/Bibata_Cursor/compare/v1.0.1...v1.0.2
[bibata v1.0.1]: https://github.com/ful1e5/Bibata_Cursor/compare/v1.0.0...v1.0.1
[bibata v1.0.0]: https://github.com/ful1e5/Bibata_Cursor/compare/v0.4.2...v1.0.0
[bibata v0.4.2]: https://github.com/ful1e5/Bibata_Cursor/compare/v0.4.2.beta.1...v0.4.2
[bibata v0.4.2.beta.1]: https://github.com/ful1e5/Bibata_Cursor/compare/v0.4.2.alpha.2...v0.4.2.beta.1
[bibata v0.4.2.alpha.2]: https://github.com/ful1e5/Bibata_Cursor/compare/v0.4.2.alpha.1...v0.4.2.alpha.2
[bibata v0.4.2.alpha.1]: https://github.com/ful1e5/Bibata_Cursor/compare/v0.4.1...v0.4.2.alpha.1
[bibata v.0.4.1]: https://github.com/ful1e5/Bibata_Cursor/compare/v0.3.1...v0.4.1
[bibata v0.3.1]: https://github.com/ful1e5/Bibata_Cursor/compare/v0.3...v0.3.1
[bibata v0.3]: https://github.com/ful1e5/Bibata_Cursor/tree/v0.3
