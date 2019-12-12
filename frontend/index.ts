import { frag, on, attr, mount, styleEl, cx } from 'marycat'
import { header, div, main } from './bindings'
import { store } from './store'
import { FormAuth } from './components/form-auth'
import { Button } from './components/button'
import { client } from './api'
import * as router from './router'
import { GET_ME, SIGNOUT } from './queries'
import { Me } from './graphql-types/Me'
import { Signout } from './graphql-types/Signout'
import css from './index.css'

(function start() {
  router.update()
  window.onhashchange = router.update

  client.query<Me>({ query: GET_ME })
    .then(({ data }) => data.me && (store.user.v = data.me))
    .catch(_=>_)

  const logout = () =>
    client.query<Signout>({ query: SIGNOUT })
      .then(() => store.user.v = null)
      .catch(_=>_)

  const app = frag()
    (styleEl(css))
    (header(cx`header`)
      (div(cx`header-logo`)('Lecture'))
      (div(cx`header-auth`)
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
}())

