# 1. Overview

## 1.1. Background

The RUC-MESSAGEix-China (RMC) model is an energy-economy-environment (E3) model for China based on the open-source modeling framework MESSAGEix ([IIASA ECE Programme, 2020](./references.md)). It is co-developed and maintained by Prof. Zhou Wenji’s group at the School of Applied Economics, Renmin University of China (RUC), and Prof. Ren Hongtao at the School of Business, East China University of Science and Technology (ECUST).

## 1.2. Basic principles

The main RMC model is based on the globally renowned integrated assessment modeling framework MESSAGEix, which is developed and maintained by the International Institute for Applied Systems Analysis (IIASA), and widely used for integrated assessment models (IAMs) and energy system models (ESMs) ([IIASA ECE Programme, 2020](./references.md)). The sub-modules for different sectors (e.g., RMC|Steel and RMC|Transport) are developed in various approaches and linked with the main RMC model in multiple ways. MESSAGEix is highly flexible and suitable for constructing local, national, multi-regional, or global energy system models, and can reflect the dynamic evolution of energy systems over multiple periods, as well as incorporate rich technological details. While typically used for analyzing energy systems at regional levels, this framework can also be applied to study individual energy sectors, such as electricity or heat.

As an optimization modeling framework, its mathematical principle involves an overall objective function to minimize the total discounted system cost over the whole modeling horizon, which aggregates the costs of all energy technologies, including investment and operating costs of technologies, extraction costs of exhaustible resources, and generation costs of renewable energy, emission taxes, and other expenditures. In addition, constraints can be added as needed, such as limiting total carbon emissions from the energy system (or carbon emissions from individual technologies). 

More features and functions of MESSAGEix can be found in its online documentation[^1] and related literature, e.g., ([Huppmann et al., 2019](./references.md)). The source code is available from the Git repository[^2].

## 1.3. Spatial-temporal resolution

The RMC model currently covers 31 provincial-level administrative regions in mainland China (excluding Hong Kong, Macao, and Taiwan for now), accounting for the energy system structure, economic development patterns, and resource endowments, among other factors, at the provincial scale.

To assess the systemic impact of China’s carbon-neutral goals, the current version of RMC is calibrated to 2022 and has a modeling horizon from 2025 to 2060 with a five-year time interval. Thanks to the flexibility of the MESSAGEix framework, both the time range and time step can be adjusted to meet various research needs.

[^1]: [The MESSAGEix documentation.](https://docs.messageix.org/en/latest/index.html)
[^2]: [MESSAGEix GitHub repository.](https://github.com/iiasa/message_ix)
