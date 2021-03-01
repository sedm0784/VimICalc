let s:path = expand('<sfile>:h:h')

" FIXME: Support .vimicalc file extension and include some efficient
"        mechanism for saving

function vimicalc#initialise() abort
  " FIXME: Set it to nofile unless saved?
  augroup VimICalcBuffer
    autocmd!
    execute 'autocmd TextChanged,TextChangedI <buffer> py3file '..s:path..'/plugin/vimicalc.py'
  augroup END
  redraw
  echom "Welcome to VimICalc"
endfunction

function vimicalc#new() abort
  new
  set filetype=vimicalc
endfunction

