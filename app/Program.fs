open ocr

// For more information see https://aka.ms/fsharp-console-apps
printfn "Hello from F#"

let input = """
    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|
"""
parse input |> printfn "%A"

printfn "%i" (Characters.one.Split("\n").Length)
