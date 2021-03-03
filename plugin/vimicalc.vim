" vimicalc.vim - VimICalc
" Author: Rich Cheng <http://whileyouweregone.co.uk>
" Homepage: http://github.com/sedm0784/VimICalc
" Copyright: © 2021 Rich Cheng
" Licence: VimICalc uses the Vim licence.
" Version: 0.1.0

" Set cpoptions so we can use line continuation
let s:save_cpo = &cpoptions
set cpoptions&vim

if exists('g:loaded_vimicalc')
      \ || &compatible
      \ || v:version < 700

  " Restore user's cpoptions setting
  let &cpoptions = s:save_cpo
  unlet s:save_cpo
  finish
endif

let g:loaded_vimicalc = 1

if !has('python3_compiled')
  command VimICalc echoerr "VimICalc requires Vim to be compiled with support for Python 3."

  " Restore user's cpoptions setting
  let &cpoptions = s:save_cpo
  unlet s:save_cpo
  finish
endif

command VimICalc call vimicalc#new()

augroup VimICalc
  autocmd!
  autocmd FileType vimicalc call vimicalc#initialise()
augroup END

" Restore user's cpoptions setting
let &cpoptions = s:save_cpo
unlet s:save_cpo
