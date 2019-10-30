import { frag, on, attr, mount, styleEl } from 'marycat'
import { header, div, main } from './bindings'
import { store, User } from './store'
import { FormAuth } from './components/form-auth'
import { Button } from './components/button'
import { get } from './api'
import * as router from './router'
import css from './index.css'

router.update()
window.onhashchange = router.update

get<User>('/auth/userdata/')
  .then(data => store.user.v = data)
  .catch(_=>_)

const logout = () =>
  get('/auth/logout/')
    .then(() => store.user.v = null)

const app = frag()
  (styleEl()(css))
  (header('.header')
    (div('.header-logo')('🌌 Lecture'))
    (div('.header-auth')
      (store.user.map(v => v ? [
        Button.new()(v.username),
        Button.new('Выйти')(on('click', logout)),
      ] :
        Button.new('Войти'))
      )
    )
    (store.user.map(v => !v &&
      FormAuth.new()(attr('tabindex', 0))
    ))
  )
  (main()
    (router.element.map(el => el || ''))
  )
mount(document.body, app)
