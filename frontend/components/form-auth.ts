import { State, customElement, PipeFn, styleEl, on, attr, cx, name } from 'marycat'
import { form, div, input, button } from '../bindings'
import { Toggle } from './toggle'
import { Button } from './button'
import { store } from '../store'
import { client } from '../api'
import { SIGNUP, SIGNIN } from '../queries'
import { Signup, SignupVariables } from '../graphql-types/Signup'
import { Signin, SigninVariables } from '../graphql-types/Signin'
import css from './form-auth.css'

type FormMode = '🔑' | '👽'

function viewFormAuth(h: PipeFn<ShadowRoot>) {
  const option: State<FormMode> = new State('🔑')
  const errors = new State({ main: '', email: '', name: '' })
  const submit = async (e: Event) => {
    const entries = new FormData(e.target as HTMLFormElement)
    const data = Object.fromEntries(entries)
    const variables = {
      name: data.name.toString(),
      email: data.email.toString(),
      password: data.password.toString(),
    }
    try {
      if (option.v === '👽') {
        const { data: { signup } } = await client.query<Signup, SignupVariables>({
          query: SIGNUP, variables,
        })
        if (!signup) return
        const { user, conflict } = signup
        if (user) store.user.v = user
        else if (conflict) {
          errors.v = {
            ...errors.v,
            email: conflict.email ? 'Email занят' : '',
            name: conflict.name ? 'Никнейм занят' : '',
          }
        }
      } else {
        const { data: { signin } } = await client.query<Signin, SigninVariables>({
          query: SIGNIN, variables,
        })
        if (signin && signin.user) store.user.v = signin.user
      }
    } catch (err) {
      console.log(err)
      errors.v = { ...errors.v, main: 'Не удаётся войти' }
    }
  }
  return h
  (styleEl(css))
  (form()
    (on('submit', submit, { prevent: true }))
    (div(cx`error`)(errors._.main.or('')))
    (Toggle.new()
      (Toggle.prop('tabs', ['🔑', '👽']))
      (Toggle.on('change', e => option.v = <FormMode>e.detail))
    )
    (input(name`email`)
      (attr('type', 'email'))
      (attr('placeholder', 'Email'))
      (attr('required', true))
      ((el: HTMLInputElement) => errors.sub(v => el.setCustomValidity(v.email)))
    )
    (input(name`passwor`)
      (attr('type', 'password'))
      (attr('placeholder', 'Пароль'))
      (attr('required', true))
    )
    (option.map(v => v === '👽' &&
      (input(name`password_again`)
        (attr('type', 'password'))
        (attr('placeholder', 'Повторите пароль'))
        (attr('required', true))
      )
      (input(name`name`)
        (attr('placeholder', 'Никнейм'))
        (attr('required', true))
        ((el: HTMLInputElement) => errors.sub(v => el.setCustomValidity(v.name)))
      )
    ))
    (button()
      (Button.new('Продолжить'))
    )
  )
}
export const FormAuth = customElement('lecture-form-auth', viewFormAuth)
