$(document).ready(() => {
  $('textarea.query').focus()
})

$('textarea.query').on('keypress', evt => {
  if ((evt.metaKey || evt.ctrlKey) && evt.keyCode === 13) {
    sendQuery(evt.target.value)
  }
})

let sendQuery = co.wrap(function *(query) {
  let response = yield fetch('http://localhost:8080/query', {
    method: 'POST',
    body: query,
  })
  let result = yield response.json()
  let text = JSON.stringify(result, null, 2)
  $('textarea.result').text(text)
})
