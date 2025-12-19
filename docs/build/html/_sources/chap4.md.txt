# 4. Iron and steel module: RMC|Steel

RMC|Steel is a sectoral module within the RMC model family that models the low-carbon transition of China's iron and steel industry. It is designed to analyze the evolution of supply and demand, technological composition, energy structure, and the demand for specific energy carriers (such as hydrogen) in China’s steel industry during its low-carbon transition. The module is also implemented in MESSAGEix and covers 31 provincial-level administrative regions as in the RMC main model. It incorporates, in a bottom-up manner, the major production processes and key technological details of the steel sector, and has been calibrated using empirical historical data on production capacity, output, and technology costs.

## 4.1. Model structure


```{figure} _static/fig_4_1.png
---
name: Fig. 4-1
align: center
---
Fig. 4-1: Reference energy system of RMC|Steel Model.
```

As shown in {ref}`Fig. 4-1 <Fig. 4-1>`, the RMC|Steel model mainly models raw material processing, pig iron smelting, and crude steel smelting, and does not involve the subsequent processing of steel coils, billets, and other products. Among them, raw material processing mainly includes:
- Coking (coking)
- Calcination of limestone (calcin)
- Sintering and pelletizing of iron ore (sint_pelle)

The principal ironmaking technologies include:
- Blast furnace ironmaking (bf)
- Hydrogen-enriched blast furnace ironmaking (bf_h2)
- Natural gas-based direct reduced iron (dri)
- Hydrogen-based direct reduced iron (hdri)
- Hydrogen-based direct smelting reduction (hmr)

The main steelmaking technologies include:
- Basic oxygen furnace steelmaking (bof)
- Electric arc furnace steelmaking using scrap as the primary feedstock (eaf_scrap)
- Electric arc furnace steelmaking using DRI as the main feedstock (eaf_spg)

For BF, DRI, and BOF facilities, carbon capture and storage (CCS) technologies can be incorporated to mitigate CO<sub>2</sub> emissions. The BF facilities can also be retrofitted with hydrogen injection systems to achieve partial hydrogen substitution. In addition, the model provides a detailed breakdown of hydrogen production pathways, distinguishing among coal gasification, natural gas reforming, and water electrolysis from a technological perspective, each of which can be coupled with corresponding CCS technologies.

The input–output relationships among these major processes and technologies are summarized in {ref}`Table 4-1 <Table 4-1>`.

```{table} Table 4-1: RMC|Steel main technology input and output.
:name: Table 4-1

| Technology | Imput | Output |
| :--- | :--- | :--- |
| BF | coke, elec, raw iron, qklime | molten iron |
| DRI | h2, raw iron | sponge iron |
| BOF | molten iron, elec, qklime | crude steel |
| EAF (sponge iron) | sponge iron, elec | crude steel |
| EAF (scrap) | scrap, elec | crude steel |
| Coal to H<sub>2</sub> | coal, elec | H<sub>2</sub> |
| Gas to H<sub>2</sub> | ch4, elec | H<sub>2</sub> |
| Electrolysis | elec, water | H<sub>2</sub> |
```


## 4.2. Parameter settings

```{table} Table 4-2: Capital expenditures（CAPEX）
:name: Table 4-2

| Technology | CAPEX | Unit | Data source |
| :--- | :--- | :--- | :--- |
| Sintering/pelletizing | 45.87 | M$/Mtpa | [Steelonthenet, 2023](./references.md) |
| Limestone Calcination | 109.6 | M$/Mtpa | [Chumin, 2025](./references.md) |
| Coking | 446.2 | M$/Mtpa | [Reliable Plant, 2008](./references.md) |
| BF iron-making | 211 | M$/Mtpa | [IEA-ETSAP, 2010a](./references.md) |
| BF w/ H<sub>2</sub> injection | 40 | M$/Mtpa | - |
| BF w/ CCS | 80.24 | M$/Mtpa | [He et al., 2025; Wang et al., 2025](./references.md) |
| H-DRI | 580 | M$/Mtpa | [Christoph Heinemann et al., 2024](./references.md) |
| BOF steel-making | 100 | M$/Mtpa | [IEA-ETSAP, 2010](./references.md) |
| BOF w/ CCS | 80.24 | M$/Mtpa | [He et al., 2025](./references.md) |
| EAF (using DRI as main feedstock) | 143 | M$/Mtpa | [Steelonthenet.com, 2025](./references.md) |
| EAF (using scrap as main feedstock) | 143 | M$/Mtpa | [Steelonthenet.com, 2025](./references.md) |
| Coal to H<sub>2</sub> | 10692 | M$/Mtpa | [IEA, 2020; Energy Transitions Commission, 2023](./references.md) |
| Coal to H<sub>2</sub> w/ CCS | 444 | M$/Mtpa | [IEA, 2020](./references.md) |
| Gas to H<sub>2</sub> | 3641.3 | M$/Mtpa | [IEA, 2020](./references.md) |
| Gas to H<sub>2</sub> w/ CCS | 2693<br>(1488.5 in 2050) | M$/Mtpa | [IEA, 2020](./references.md) |
| Electrolysis | 8296.5<br>(3583.1 in 2050) | M$/Mtpa | [IEA, 2020](./references.md) |
```

```{table} Table 4-3: Fixed operation expenditures
:name: Table 4-3

| Technology | Fixed OPEX | Unit | Data source |
| :--- | :--- | :--- | :--- |
| Sintering/pelletizing | 1.835 | M$/Mtpa | [Arasto, 2015](./references.md) |
| Limestone Calcination | 8.05 | M$/Mtpa | [AGICO Cement Plant Equipment, 2025](./references.md) |
| Coking | 17.18 | M$/Mtpa | [Gallaher, Depro and Agency, 2002](./references.md) |
| BF iron-making | 14.14 | M$/Mtpa | [Gallaher, Depro and Agency, 2002; IEA, 2013](./references.md) |
| BF w/ H<sub>2</sub> injection | 10 | M$/Mtpa | - |
| BF w/ CCS | 4.07 | M$/Mtpa | [IEA, 2013](./references.md) |
| H-DRI | 20 | M$/Mtpa | [Steelonthenet.com, 2025](./references.md) |
| BOF steel-making | 15.45 | M$/Mtpa | [IEA Greenhouse Gas R&D Programme, 2024](./references.md) |
| BOF w/ CCS | 2.16 | M$/Mtpa | [IEA, 2013](./references.md) |
| EAF (using DRI as main feedstock) | 81.24 | M$/Mtpa | [Vogl, Åhman and Nilsson, 2018; Benavides et al., 2024](./references.md) |
| EAF (using scrap as main feedstock) | 81.24 | M$/Mtpa | [Vogl, Åhman and Nilsson, 2018; Benavides et al., 2024](./references.md) |
| Coal to H<sub>2</sub> | 433 | M$/Mtpa | [Shao Le et al., 2024](./references.md) |
| Coal to H<sub>2</sub> w/ CCS | 18 | M$/Mtpa | - |
| Gas to H<sub>2</sub> | 454.5 | M$/Mtpa | [Shao Le et al., 2024](./references.md) |
| Gas to H<sub>2</sub> w/ CCS | 50.2 | M$/Mtpa | - |
| Electrolysis | 182.5 | M$/Mtpa | [IEA, 2020](./references.md) |
```

```{table} Table 4-4: Variable operation expenditures
:name: Table 4-4

| Technology | Variable OPEX | Unit | Data source |
| :--- | :--- | :--- | :--- |
| Iron ore supply | 110.61 | M$/Mt | [Trading Economics, 2025](./references.md) |
| Limestone supply | 19.59 | M$/Mt | [kq81.com, 2025](./references.md) |
| Coal supply | 195.89 | M$/Mt | [National Bureau of Statistics of China, 2025](./references.md) |
| Natural gas supply | 694 | M$/Mt | [CEIC Data, 2025](./references.md) |
| Electricity supply | 0.085 | M$/GWh | [State-owned Assets Supervision and Administration Commission of the State Council, 2020](./references.md) |
| Water supply | 0.676 | M$/Mt | [CEIC Data, 2025](./references.md) |
| Scrap supply | 349.8 | M$/Mt | [CSteelNews, 2025](./references.md) |
| Sintering/pelletizing | 20 | M$/Mt | [Rahbari et al., 2025](./references.md) |
| Coal to H<sub>2</sub> | 434.1 | M$/Mt | [Shao Le et al., 2024](./references.md) |
| Coal to H<sub>2</sub> w/ CCS | 0 | M$/Mt | - |
| Gas to H<sub>2</sub> | 338.5 | M$/Mt | [Shao Le et al., 2024](./references.md) |
| Gas to H<sub>2</sub> w/ CCS | 0 | M$/Mt | - |
| Electrolysis | 0 | M$/Mt | - |
```

```{table} Table 4-5: Carbon emission factors
:name: Table 4-5

| Technology | Emission factor | Unit | Data source |
| :--- | :--- | :--- | :--- |
| Sintering/pelletizing | 0.2 | t-CO<sub>2</sub>/t-output | [CSteelNews, 2023; Steelonthenet, 2025; ZHAO Zedong, LI Jiaxuan, and LI Yuanye, 2025](./references.md) |
| Limestone Calcination | 1 | t-CO<sub>2</sub>/t-output | [Shenlan Environmental Protection Industry Development Co., Ltd., 2025](./references.md) |
| Coking | 0.794 | t-CO<sub>2</sub>/t-output | [Steelonthenet, 2025](./references.md) |
| BF iron-making | 1.22 | t-CO<sub>2</sub>/t-output | [Steelonthenet, 2025](./references.md) |
| BF w/ H<sub>2</sub> injection | 0.67 | t-CO<sub>2</sub>/t-output | [Zhang et al., 2024; OECD, 2025](./references.md) |
| BF w/ CCS | 0.0523 | t-CO<sub>2</sub>/t-output | [Santos et al., 2013](./references.md) |
| H-DRI | 0.04 | t-CO<sub>2</sub>/t-output | [Rechberger et al., 2020](./references.md) |
| BOF steel-making | 0.181 | t-CO<sub>2</sub>/t-output | [Nancy Margolis and Ross Brindle, 2000; European Commission. Joint Research Centre., 2022; steelonthenet, 2025](./references.md) |
| BOF w/ CCS | 0.03 | t-CO<sub>2</sub>/t-output | [Butterworth, 2024](./references.md) |
| EAF (using DRI as main feedstock) | 0.03 | t-CO<sub>2</sub>/t-output | [European Commission. Joint Research Centre., 2022](./references.md) |
| EAF (using scrap as main feedstock) | 0.03 | t-CO<sub>2</sub>/t-output | [European Commission. Joint Research Centre., 2022](./references.md) |
| Coal to H<sub>2</sub> | 20.1 | t-CO<sub>2</sub>/t-output | [IEA, 2019](./references.md) |
| Coal to H<sub>2</sub> w/ CCS | 2.1 | t-CO<sub>2</sub>/t-output | [IEA, 2019](./references.md) |
| Gas to H<sub>2</sub> | 10.13 | t-CO<sub>2</sub>/t-output | [Baltac et al., 2022](./references.md) |
| Gas to H<sub>2</sub> w/ CCS | 2.32 | t-CO<sub>2</sub>/t-output |[Baltac et al., 2022](./references.md) |
```
