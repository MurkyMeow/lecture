import { el } from 'marycat'
import * as router from './router'

window.div = el('div')
window.img = el('img')
window.span = el('span')
window.main = el('main')
window.header = el('header')
window.section = el('section')

import './pages/page-index'
import './pages/page-about'

router.update(location.pathname)
