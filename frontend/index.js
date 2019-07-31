import { State, el, _if, form, input, fragment } from 'marycat'
import { Button } from './components/button'
import { FormAuth } from './components/form-auth'
import * as router from './router'

import './index.css';

window.div = el('div')
window.img = el('img')
window.span = el('span')
window.main = el('main')
window.header = el('header')
window.section = el('section')
window.form = form
window.input = input

router.update()

const user = new State(null)
const signup = new State(true)

const app = fragment()
  (header('.header')
    (div('.header-logo')('🌌 Lecture'))
    (div('.header-auth')
      (_if(user)
        (Button().text('username'))
        (Button().text('Выйти'))
      .else()
        (Button().text('Создать аккаунт').click(() => signup.v = true))
        (Button().text('Войти').click(() => signup.v = false))
      )
    )
    (FormAuth().signup(signup).tabindex(0))
  )
  (main()
    (router.element)
  )
app(document.body)
