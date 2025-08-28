import marimo

__generated_with = "0.15.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import sympy as sy
    return (sy,)


@app.cell
def _(sy):
    a = 5

    print(sy.isprime(a))
    return


@app.cell
def _(sy):
    N = 10
    lista_numeri = [x for x in range(N+1)]

    primi = [x for x in lista_numeri if sy.isprime(x)]
    print(primi)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
