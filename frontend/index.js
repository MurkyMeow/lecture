import { el, _if, form, input, fragment } from 'marycat'
import { store } from './store'
import { Button } from './components/button'
import { FormAuth } from './components/form-auth'
import { get } from './api'
import * as router from './router'

import './index.css';

window.h1 = el('h1')
window.div = el('div')
window.img = el('img')
window.pre = el('pre')
window.span = el('span')
window.main = el('main')
window.iframe = el('iframe')
window.button = el('button')
window.header = el('header')
window.article = el('article')
window.section = el('section')
window.form = form
window.input = input

router.update()

get('/auth/userdata/')
  .then(data => store.user.v = data)
  .catch(_=>_)

const logout = () =>
  get('/auth/logout/')
    .then(() => store.user.v = null)

const app = fragment()
  (header('.header')
    (div('.header-logo')('🌌 Lecture'))
    (div('.header-auth')
      (_if(store.user)
        (Button().text(store.user.or({})._`username`))
        (Button().text('Выйти').click(logout))
      .else()
        (Button().text('Войти'))
      )
    )
    (_if(store.user.not())
      (FormAuth().tabindex(0))
    )
  )
  (main()
    (router.element)
  )
app.connect(document.body)
