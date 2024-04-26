// [JS-A01] Considere três notas (n1, n2, n3) e seus respectivos pesos (p1, p2, p3). Calcule a média
// ponderada das notas e atribua o resultado à variável "media". Após o cálculo, exiba a média
// ponderada no console.

// OBS: Para calcular a média ponderada multiplica os valores das notas pelos valores dos pesos,
// e divide pelas somas de todos os pesos. Lembre-se de declarar valores para os pesos e para as notas.

let n1 = 50
let n2 = 80
let n3 = 70

let p1 = 10
let p2 = 9
let p3 = 8

let notas = (n1 * p1) + (n2 * p2) + (n3 * p3)
let pesos = p1 + p2 + p3
let media = notas / pesos

console.log(`A média ponderada é: ${media}.`)