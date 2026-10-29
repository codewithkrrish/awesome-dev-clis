# awesome-dev-clis

A curated list of command-line tools I actually use, or want to start using.
Every entry here earned its place because it saved me real time — not
because it showed up on some top-10 blog post.

I kept hitting the same problem: I'd hear about a great CLI tool, forget its
name a week later, and end up re-Googling it from scratch. So I started
keeping my own list, grouped by the job I reach for it for. This repo is that
list, cleaned up and kept current.

## Contents

- [Files and search](#files-and-search)
- [Text and data](#text-and-data)
- [Git and GitHub](#git-and-github)
- [Network](#network)
- [System and processes](#system-and-processes)
- [Terminal life](#terminal-life)
- [Modern replacements for old commands](#modern-replacements-for-old-commands)
- [My starter kit](#my-starter-kit)
- [Contributing](#contributing)
- [License](#license)

## Files and search

- [ripgrep](https://github.com/BurntSushi/ripgrep) — Search through code faster than grep, and it respects your `.gitignore` by default so you don't wade through `node_modules`. `cargo install ripgrep`
- [fd](https://github.com/sharkdp/fd) — A simpler, faster `find`. Sensible defaults, colour output, and it understands `.gitignore` too. `cargo install fd-find`
- [fzf](https://github.com/junegunn/fzf) — Fuzzy finder for everything: files, history, processes, git branches. Once it's in your muscle memory you can't go back. `brew install fzf`
- [zoxide](https://github.com/ajeetdsouza/zoxide) — Smarter `cd` that learns which directories you actually visit. Type `z proj` instead of the full path. `cargo install zoxide`
- [bat](https://github.com/sharkdp/bat) — `cat` with syntax highlighting, line numbers, and git markers. Makes reading code in a terminal pleasant. `cargo install bat`
- [eza](https://github.com/eza-community/eza) — A modern `ls` with colours, icons, and git status baked in. `cargo install eza`
- [dust](https://github.com/bootandy/dust) — See where your disk space went, as a readable tree, without waiting on `du`. `cargo install du-dust`
- [ncdu](https://dev.yorhel.nl/ncdu) — Interactive disk usage browser. When the disk is full and you need to find the culprit now. `apt install ncdu`
- [rclone](https://rclone.org/) — Sync files to and from basically any cloud storage from the terminal, with one consistent interface. `curl https://rclone.org/install.sh | sudo bash`
- [rsync](https://rsync.samba.org/) — Still the right tool for copying a directory tree to a server and resuming when it breaks halfway. `apt install rsync`

## Text and data

- [jq](https://github.com/jqlang/jq) — The JSON processor. If you work with APIs from the terminal, this one is non-negotiable. `apt install jq`
- [yq](https://github.com/mikefarah/yq) — `jq` for YAML (and TOML, XML, and more). Same idea, same muscle memory. `brew install yq`
- [miller](https://github.com/johnkerl/miller) — `awk`/`cut`/`sort` for CSV and JSON, but with named columns so you stop counting field numbers. `apt install miller`
- [csvkit](https://github.com/wireservice/csvkit) — A whole set of small tools for CSV files: inspect, convert, query with SQL, diff. `pip install csvkit`
- [sd](https://github.com/chmln/sd) — Find-and-replace across files with a syntax that reads like what you mean, unlike sed's escaping maze. `cargo install sd`
- [pandoc](https://pandoc.org/) — Convert documents between formats: Markdown to PDF, HTML to docx, and about forty others. `apt install pandoc`
- [glow](https://github.com/charmbracelet/glow) — Render Markdown beautifully in the terminal when you want to actually read a README instead of skimming raw text. `brew install glow`
- [fx](https://github.com/antonmedv/fx) — Interactive JSON viewer: expand and collapse nodes with the keyboard instead of paging through a wall of text. `brew install fx`

## Git and GitHub

- [gh](https://cli.github.com/) — GitHub's official CLI. Create repos, open PRs, check CI status, all without leaving the terminal. `apt install gh`
- [lazygit](https://github.com/jesseduffield/lazygit) — A terminal UI for git that makes staging hunks, rebasing, and fixing a messy branch genuinely quick. `brew install lazygit`
- [git-delta](https://github.com/dandavison/delta) — Diffs with syntax highlighting and side-by-side layout. Your `git log -p` becomes readable. `cargo install git-delta`
- [tig](https://github.com/jonas/tig) — Text-mode interface for git: browse history, blame, and stashes without a GUI. `apt install tig`
- [gitleaks](https://github.com/gitleaks/gitleaks) — Scan a repo for accidentally committed secrets before someone else finds them. `brew install gitleaks`
- [pre-commit](https://pre-commit.com/) — Run linters and formatters automatically on every commit so bad code never lands in the first place. `pip install pre-commit`

## Network

- [httpie](https://httpie.io/) — A friendlier curl for APIs: readable syntax, coloured output, JSON by default. `pip install httpie`
- [curl](https://curl.se/) — The one tool that can talk to anything over HTTP. You already have it; learn its flags and half your debugging gets easier. `apt install curl`
- [aria2](https://aria2.github.io/) — Download manager with resume, parallel connections, and metalink support. For big files over shaky connections. `apt install aria2`
- [dog](https://github.com/ogham/dog) — DNS lookups with coloured, readable output. `dig` works, but dog is easier to scan at a glance. `cargo install dog`
- [bandwhich](https://github.com/imsnif/bandwhich) — See which process is eating your bandwidth, live, per connection. `cargo install bandwhich`
- [mosh](https://mosh.org/) — SSH that survives flaky wifi and roaming between networks without dropping your session. `apt install mosh`
- [http-server](https://github.com/http-party/http-server) — Serve the current directory over HTTP in one command when you just need to preview a static site. `npm install -g http-server`

## System and processes

- [btop](https://github.com/aristocratos/btop) — A resource monitor that looks good and shows CPU, memory, disks, and network in one view. `apt install btop`
- [procs](https://github.com/dalance/procs) — A modern `ps` with colour, tree view, and columns you can actually read. `cargo install procs`
- [htop](https://htop.dev/) — The classic interactive process viewer. If btop feels like too much, htop is the safe pick. `apt install htop`
- [duf](https://github.com/muesli/duf) — Disk usage for humans: a clean table of every mount instead of `df`'s cramped columns. `brew install duf`
- [tldr](https://github.com/tldr-pages/tldr) — Community cheat sheets for commands: practical examples first, man-page theory later. `npm install -g tldr`
- [cheat](https://github.com/cheat/cheat) — Like tldr but you can add your own cheat sheets, which is where it gets genuinely useful. `brew install cheat`
- [watch](https://man7.org/linux/man-pages/man1/watch.1.html) — Re-run a command every few seconds. Boring, old, and used daily for watching logs and build output. `apt install procps`

## Terminal life

- [tmux](https://github.com/tmux/tmux) — Terminal multiplexer: split panes, persistent sessions, detach and come back later. The single biggest terminal productivity jump there is. `apt install tmux`
- [starship](https://starship.rs/) — A fast, customisable shell prompt that shows git branch, language version, and status without slowing your shell down. `cargo install starship`
- [atuin](https://github.com/atuinsh/atuin) — Shell history that syncs across machines and is actually searchable, instead of `Ctrl+R` roulette. `cargo install atuin`
- [gum](https://github.com/charmbracelet/gum) — Build interactive shell scripts with prompts, pickers, and spinners, without writing a TUI from scratch. `brew install gum`
- [zellij](https://zellij.dev/) — A newer take on tmux with a friendlier default layout and built-in plugin system. Worth trying if tmux's keybindings never clicked for you. `cargo install zellij`
- [direnv](https://direnv.net/) — Load and unload environment variables automatically when you enter a project directory. No more sourcing `.env` files by hand. `apt install direnv`

## Modern replacements for old commands

These are the new tools that do an old job better. I keep them in one place
because this is the section I send to friends most often.

- [ripgrep](https://github.com/BurntSushi/ripgrep) — replaces `grep` — faster, respects `.gitignore`. `cargo install ripgrep`
- [fd](https://github.com/sharkdp/fd) — replaces `find` — simpler syntax, colour output. `cargo install fd-find`
- [bat](https://github.com/sharkdp/bat) — replaces `cat` — syntax highlighting, git markers. `cargo install bat`
- [eza](https://github.com/eza-community/eza) — replaces `ls` — icons, git status, tree view. `cargo install eza`
- [dust](https://github.com/bootandy/dust) — replaces `du` — readable tree of disk usage. `cargo install du-dust`
- [duf](https://github.com/muesli/duf) — replaces `df` — clean table of mounts. `brew install duf`
- [procs](https://github.com/dalance/procs) — replaces `ps` — colour, tree view, readable columns. `cargo install procs`
- [btop](https://github.com/aristocratos/btop) — replaces `top` — full system view in one screen. `apt install btop`
- [zoxide](https://github.com/ajeetdsouza/zoxide) — replaces `cd` — learns where you go. `cargo install zoxide`
- [sd](https://github.com/chmln/sd) — replaces `sed` for simple replacements — no escaping maze. `cargo install sd`
- [dog](https://github.com/ogham/dog) — replaces `dig` — coloured, scannable DNS output. `cargo install dog`
- [httpie](https://httpie.io/) — replaces `curl` for quick API calls — readable syntax, JSON by default. `pip install httpie`
- [tldr](https://github.com/tldr-pages/tldr) — replaces reaching for `man` first — examples before theory. `npm install -g tldr`

## My starter kit

If I set up a fresh machine tomorrow, these go on first, in this order.
Everything else on this list is a "later, when I need it".

1. `git`, `curl`, `tmux`, `starship` — the base layer.
2. `ripgrep`, `fd`, `fzf`, `zoxide` — finding things fast.
3. `bat`, `eza`, `jq` — reading things comfortably.
4. `gh`, `lazygit`, `git-delta` — working with GitHub without a browser.
5. `btop`, `duf`, `tldr` — keeping the machine and my memory healthy.

Install the lot on Debian/Ubuntu with roughly:

```bash
apt install git curl tmux jq tig htop
cargo install ripgrep fd-find bat eza zoxide starship
```

## Contributing

Found a tool that deserves a place here, or one that's gone stale? Open a
pull request. One entry per PR, and each entry needs: a link to the project,
one honest line about why it's worth installing, and an install command you
have actually tried. Entries without an install command don't get merged —
the whole point of this list is that you can go from reading to using in one
copy-paste.

Run the list checker before you push:

```bash
python3 tools/check_list.py
```

## Limitations

Honest notes, because every list like this has them:

- This list leans Linux/macOS. Windows users will find some tools available
  through winget or scoop, but I haven't verified each one there.
- Install commands are what worked for me at the time of writing; package
  names change, and a command that worked six months ago can break.
- I haven't used every tool here daily. Some are tools I reach for weekly,
  a few are ones I tried once and kept because the idea was right. The
  one-line notes say which is which only loosely — use your judgment.
- No affiliate links, no sponsored entries. If a tool ever stops being
  maintained, it should come off the list, not stay for nostalgia.

## License

MIT — see [LICENSE](LICENSE).

## Author

Built by [Krrish](https://github.com/codewithkrrish). If this list saved you
a search, a star helps it reach the next person who needs it.
