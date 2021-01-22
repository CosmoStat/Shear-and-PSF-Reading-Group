# Sources of the PSF

```{warning}
In progress!
```

_(Note) Here we will give the definition of the PSF and go through the different contributors of the PSF._

## Definition

Give a definition of the PSF.

- Include two images, a space-based PSF and a ground-based PSF.
  - (can I put an Euclid-like PSF(?))



## Contributors

_(Note) Maybe add some figures illustrating the different effects after a brief description of each one._

Describe the contributors of the PSF:

## Optic level:
- Diffraction effects
- Imperfect optics
- Chromaticity
  - Optical system Chromaticity
  - Observed object SED


## Ground-based

- Atmosphere

## Space-based

- Jitter
- Attitude and Orbit Control System


## Detector level

Normally these effects are largely corrected in the image preprocessing pipeline. However, the corrections will not be perfect, and residuals from those corrections could affect the PSF modelling.

- Charge Transfer Inefficiency
- Brighter Fatter Effect
- Analog-to-Digital Unit non-linearity
- Other effects:
  - Thermal noise
  - Quantisation
  - Background estimation and subtraction


_(Note) There are several effect I don't think I will include:_
- Thermal variations (this could be included, important effect)
- Polishing errors
- variation across field because of varying bandpass (imperfect filters)
- polarisation dependence of the PSF
- Wavelength-dependent optical system components (non-reflective elements)
