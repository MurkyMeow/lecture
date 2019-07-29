import { el } from 'marycat'

window.div = el('div')
window.div = el('div')
window.img = el('img')
window.span = el('span')
window.main = el('main')
window.header = el('header')
window.section = el('section')

const app = 
  main()
    (header('.header')
      (div('.header-title')
        (span('🌠 Melior'))
      )
    )
    (div('.content')
      (section())
      (section())
      (section())
    )

app(document.body)
