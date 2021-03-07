# Definiendo modelo basico

struct Data{
    1: required Pedigree pedigree;
    2: required DataUnit dataUnit;
}

struct Pedigree{
    1: required i32 true_as_of_secs;
}

union DataUnit{
    1: Pais pais;
    2: IndicadorRecursos indicadorRecursos;
    3: Gasta gasta;
}

# Definiendo estructura Pais

struct Pais{
    1: required string nombrePais;
}

# Definiendo estructura IndicadorRecursos

struct IndicadorRecursos{
    1: required Indicadores nombreIndicador;
    2: required ValorIndicador valorIndicador;
}

enum Indicadores{
    talaArbol = 1;
    talaArbol_volumenSalvado = 2;
    talaArbol_neta = 3;
    perdidasNaturales = 4;
    incrementoBruto = 5;
    incrementoNeto = 6;
    cambioNeto = 7;
    intensidadUso = 8;
}

# Definiendo union ValorIndicador

union ValorIndicador{
    1: i32 indicadorInt;
    2: double indicadorDouble;
}

# Definiendo estructura Gasta

struct Gasta{
    1: required string nombrePais;
    2: required string nombreIndicador;
    3: required i64 nonce;
}