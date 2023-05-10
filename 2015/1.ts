export function exec(input: string) {
    let floor = 0, position = 0, positionFound = false
    for (const parenthesis of input) {
        floor += parenthesis === "(" ? 1 : -1
        if (!positionFound) {
            position += 1
            if (floor === -1) positionFound = true
        }
    }
    console.log(`Part 1: ${floor}`)
    console.log(`Part 2: ${position}`)
}