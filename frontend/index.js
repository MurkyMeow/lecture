import { el, fragment } from 'marycat'
import * as router from './router'

import './index.css';

window.div = el('div')
window.img = el('img')
window.span = el('span')
window.main = el('main')
window.header = el('header')
window.section = el('section')

router.update()

const app = fragment()
  (header('.header')
    (div('.header-title')('🌌 lecture'))
  )
  (main()
    (router.element)
  )
app(document.body)
