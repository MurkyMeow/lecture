import { State, el, _if, form, input, fragment } from 'marycat'
import { Button } from './components/button'
import { FormAuth } from './components/form-auth'
import * as router from './router'

import './index.css';

window.h1 = el('h1')
window.div = el('div')
window.img = el('img')
window.span = el('span')
window.main = el('main')
window.button = el('button')
window.header = el('header')
window.section = el('section')
window.textarea = el('textarea')
window.form = form
window.input = input

router.update()

const user = new State(null)

const app = fragment()
  (header('.header')
    (div('.header-logo')('🌌 Lecture'))
    (div('.header-auth')
      (_if(user)
        (Button().text('username'))
      .else()
        (Button().text('Войти'))
      )
    )
    (FormAuth().tabindex(0))
  )
  (main()
    (router.element)
  )
app.connect(document.body)
