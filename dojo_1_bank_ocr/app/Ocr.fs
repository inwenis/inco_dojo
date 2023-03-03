module ocr

open System
open Characters

let parseDigit (input: string)  =
    match input with
    | Characters.one -> Some 1
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
