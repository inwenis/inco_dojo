module ocr

open System
open Characters

let parseDigit (input: string)  =
    match input with
    | x when x = one -> Some 1
    | x when x = two -> Some 2
    | x when x = three -> Some 3
    | x when x = four -> Some 4
    | x when x = five -> Some 5
    | x when x = six -> Some 6
    | x when x = seven -> Some 7
    | x when x = eight -> Some 8
    | x when x = nine -> Some 9
    | x when x = zero -> Some 0
    | _ -> None
    
let parse (input: string) = 
    input.Split("\n", StringSplitOptions.RemoveEmptyEntries)
    |> Array.collect (fun l ->
        l.ToCharArray()
        |> Array.chunkBySize 3
        |> Array.mapi (fun i c -> i, c) )
    |> Array.groupBy fst
    |> Array.map snd
    |> Array.map (fun x -> x |> Array.map snd |> Array.map (fun cs -> String(cs)) |> String.concat "\n")
    |> Array.map parseDigit
    |> Array.toList
