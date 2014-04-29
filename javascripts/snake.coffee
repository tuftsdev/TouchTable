$ = jQuery
$ ->
  # Snake box responsiveness
  canvas = 0
  ctx = 0
  width = 0
  height = 0
  resize = ->
    canvas = $(".snake-boundary")
    canvas.width('90%')
    canvas.height('75%')
    ctx = canvas[0].getContext("2d")
    width = canvas.width()
    height = canvas.height()
    width = Math.round(width/10)*10
    height = Math.round(height/10)*10
    canvas.attr({'width':width, 'height':height})

  resize()
  $(window).resize(->
    resize()
  )

  cell_width = 20
  direction = "right"
  food = {}
  score = 0

  snake_array = []

  init = ->
    direction = "right"
    create_snake()
    create_food()
    score = 0

    if(typeof game_loop != "undefined")
      clearinterval(game_loop)
    game_loop = setInterval(paint, 60)

  create_snake = ->
    length = 5
    snake_array = []
    i = length-1
    while i >= 0
      snake_array.push({x:i,y:0})
      i--

  create_food = ->
    food = {
      x: Math.round(Math.random()*(width-cell_width)/cell_width),
      y: Math.round(Math.random()*(height-cell_width)/cell_width)
    }

  paint = ->
    ctx.fillStyle = '#2c3e50'
    ctx.fillRect(0,0,width,height)

    nx = snake_array[0].x
    ny = snake_array[0].y

    if(direction == "right")
      nx++
    else if(direction == "up")
      ny--
    else if(direction == "down")
      ny++
    else if(direction == "left")
      nx--

    if(false)
      console.log 'impossible'
    else
      tail = snake_array.pop()
      tail.x = nx
      tail.y = ny

    snake_array.unshift(tail)
    i = 0
    while i < snake_array.length
      c = snake_array[i]
      paint_cell(c.x,c.y)
      i++

  paint_cell = (x,y)->
    ctx.fillStyle = '#e74c3c'
    ctx.fillRect(x*cell_width, y*cell_width, cell_width, cell_width)
    ctx.strokeStyle = '#2c3e50'
    ctx.strokeRect(x*cell_width, y*cell_width, cell_width, cell_width)

  $(document).keydown((e)->
    key = e.which
    console.log key
    if key == 37 && direction != "right"
      direction = "left"
    else if key == 38 && direction != "down"
      direction = "up"
    else if key == 39 && direction != "left"
      direction = "right"
    else if key == 40 && direction != "up"
      direction = "down"
  )

  init()
