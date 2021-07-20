# Definition

We can vaguely define the Point Spread Function (PSF) as the response of imaging system to a point source. The concept of PSF is used throughout many imaging applications, some of them are astronomical imaging and medical imaging. Depending on the science application the definition and its sources may vary. However, they all include the [diffraction](https://en.wikipedia.org/wiki/Diffraction) phenomena. The fact of having a non-infinite lens sets a limit on the resolution of the imaging system.

We will focus on PSFs for astronomical imaging and analyze its main sources.


## Types of variations

- __Spatial__

The variations that change as a function of the focal plane positions. These are main type of variations targeted by the PSF models. They mainly depend on the telescope's optics and the spatial correlations introduced by the atmosphere.

- __Spectral__

The PSF is a function of the wavelength. The PSF at a specific wavelength is usually called a monochromatic PSF. The observations of our telescope are integrated at all the wavelengths allowed by the filter's bandpass used. As a consequence, our observations are polychromatic. Depending if the filter's bandpass is narrow or large and the given error requirements, the modelling of the PSF spectral variations might be required (e.g. [Euclid](https://www.euclid-ec.org)) or can be neglected (e.g. [DES](https://www.darkenergysurvey.org)). 

- __Temporal__

The PSF also varies temporally. The time we are integrating the PSF is given by the exposure time. This is a fundamental parameter that will determine several characteristics of the PSF. For example, for ground-based surveys, it changes the impact of the atmosphere on the PSF. 
The instruments characteristics also change over time giving the PSF a low frequency variation. For space-based surveys where the atmosphere does not play a role, the characteristics of the instrument change over time following temperature changes for example. This makes unpractical the estimation of a single PSF model for all the exposures, as all the instrument's variability over time and its influence over the PSF should be modelled. It is common to estimate PSF models for each exposure (or several exposures) in order to tackle this low frequency temporal variations.