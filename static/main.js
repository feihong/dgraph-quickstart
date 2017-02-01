$('textarea.query').focus()

$('textarea.query').on('keypress', evt => {
  if ((evt.metaKey || evt.ctrlKey) && evt.keyCode === 13) {
    sendQuery(evt.target.value)
  }
})

let sendQuery = co.wrap(function *(query) {
  let response = yield fetch('http://localhost:8000/query', {
    method: 'POST',
    body: query,
  })
  let text = yield response.text()
  $('textarea.result').text(text)
})
