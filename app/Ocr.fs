module ocr

open Characters

let parse (input: string)  =
    if input = one then Some 1
    elif input = two then Some 2
    elif input = three then Some 3
    elif input = four then Some 4
    elif input = five then Some 5
    elif input = six then Some 6
    elif input = seven then Some 7
    elif input = eight then Some 8
    elif input = nine then Some 9
    elif input = zero then Some 0
    else None
