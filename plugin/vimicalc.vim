command VimICalc call vimicalc#new()

augroup VimICalc
  autocmd!
  autocmd FileType vimicalc call vimicalc#initialise()
augroup END
