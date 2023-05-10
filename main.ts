async function main(): Promise<void> {
  const year = prompt("Please enter the year:");
  const day = prompt("Please enter the day:");
  const input = Deno.readTextFileSync("./input.txt")

  const processData = await import(`./${year}/${day}.ts`)
  processData.exec(input)
}

if (import.meta.main) main()