syntax on

set number
set relativenumber

set autoindent
set smarttab
set expandtab
set shiftround
set shiftwidth=4
set tabstop=4
set softtabstop=4

set noswapfile
set nocompatible
filetype off

set nowrap
set showmatch

set incsearch
set nohlsearch
set ignorecase
set smartcase

set encoding=utf-8
set scrolloff=10

set cursorline
set colorcolumn=80

" Splits
set splitbelow
set splitright

" Plugins
call plug#begin()
Plug 'ap/vim-css-color'
Plug 'joshdick/onedark.vim'
Plug 'preservim/nerdtree'
Plug 'preservim/tagbar'
Plug 'ryanoasis/vim-devicons'
Plug 'tmhedberg/SimpylFold'
Plug 'tpope/vim-commentary'
Plug 'tpope/vim-surround'
Plug 'vim-airline/vim-airline'
call plug#end()

" Rendering trailing whitespace
highlight RedundantSpaces ctermbg=red guibg=red
match RedundantSpaces /\s\+$/

" Appearance
colorscheme onedark
set background=dark
hi Normal guibg=NONE ctermbg=NONE
set linespace=10

" NERDTree Setup
let NERDTreeWinSize=22
let g:NERDTreeMinimalUI=1
let g:NERDTreeDirArrows=1

" Tagbar Setup
let g:tagbar_width=22
let g:tagbar_compact=1
let g:tagbar_indent=1

" Fold Setup
set foldmethod=indent
set foldlevel=99

" Enable Folding with Space Bar
nnoremap <space> za

" Split Navigations
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-H> <C-W><C-H>
nnoremap <C-L> <C-W><C-L>

" Find
nnoremap n nzz
nnoremap N Nzz
