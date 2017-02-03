// $(document).ready(() => {
//   $('textarea.query')[0].focus()
// })

$(document).on('keypress', evt => {
  if ((evt.metaKey || evt.ctrlKey) && evt.keyCode === 13) {
    sendQuery(evt.target.value)
  }
})

let sendQuery = co.wrap(function *(query) {
  let resultTa = $('textarea.result')
  resultTa.removeClass('error').text('Executing query...')

  let response = yield fetch('http://localhost:8080/query', {
    method: 'POST',
    body: query,
  })

  if (response.status !== 200) {
    resultTa.addClass('error').text(yield response.text())
  } else {
    let responseText = yield response.text()
    try {
      let obj = JSON.parse(responseText)
      let text = JSON.stringify(obj, null, 2)
      resultTa.text(text)
    } catch (err) {
      resultTa.addClass('error').text(`${err}\n\n${responseText}`)
    }
  }
})
