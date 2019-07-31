import { State, el, _if, fragment } from 'marycat'
import { Button } from './components/button'
import * as router from './router'

import './index.css';

window.div = el('div')
window.img = el('img')
window.span = el('span')
window.main = el('main')
window.header = el('header')
window.section = el('section')

router.update()

const user = new State(null)

const app = fragment()
  (header('.header')
    (div('.header-logo')('🌌 Lecture'))
    (div('.header-auth')
      (_if(user)
        (Button().text('username'))
        (Button().text('Выйти'))
      .else()
        (Button().text('Создать аккаунт'))
        (Button().text('Войти'))
      )
    )
  )
  (main()
    (router.element)
  )
app(document.body)
