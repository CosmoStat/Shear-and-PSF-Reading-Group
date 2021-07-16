# Contributors to the PSF


## Optic level

- __Mirrors__

    - _Size_

    The size of the main mirror has a direct implicance to the size of the PSF. Following the diffraction theory, the larger the mirror for the lens, the smaller size the PSF should have. There are practical limitations on the maximal sizes of mirrors that are due to the manufacturing process. As an example, we can show the impact of the telescope's pupil diameter in the size of the PSF in the ideal Airy PSF we only take into account the diffraction phenomena. For this type of PSF we can write the Full Width Half Maximum (FWHM) as a function of the wavelength $\lambda$ and the pupil diameter $D$ as,

    $$
    \text{FWHM}_{\text{Airy}} = 1.028 \; \frac{\lambda}{D} .
    $$


    - _Aberrations_
    
    There are imperfections in the curvature of mirrors producing different types of aberrations. These introduce optical path differences for the incoming light rays producing features in the PSF. They are usually modelled using [Zernike polynomials](https://en.wikipedia.org/wiki/Zernike_polynomials) which are a sequence of polynomials that are orthogonal in the unit disk.
        
        
```{figure} ../../_static/psf_wavefron_aberrations.png
---
height: 300px
name: psf_wavefron_aberrations
---
Illustration of the optical path differences in a lens. Note that current telescopes are build with _mirrors_ but the illustration shows a _lens_. Credit: Austin Roorda.

```

```{figure} ../../_static/psf-typical-aberrations.png
---
height: 150px
name: psf-typical-aberrations
---
Typical aberrations with simulated in-focus stars with typical seeing. Credit: Aaron Roodman.

```

- __Mirrors__

    - _Polishing effects_
    
    The polishing of the mirrors aims to have a perfectly smooth surface. However, the manufacturing process is not perfect and small errors remain in the surface of the mirrors. They are sometimes referred to as _surface errors_.

```{figure} ../../_static/psf-HST-surface-errors.png
---
height: 200px
name: psf-HST-surface-errors
---
Surface errors estimated for the Hubble Space Telescope. They are in the range of +/- 30nm. Credit: {cite}`krist2011`.

```

- __Optical system__
    - _Misalignment_
    
    Misalignement of optical elements can cause a defocus of the system.  For example, in Figure 7 and 8 from {cite}`jee2011` one can see the effects of Charge-Coupled Devices (CCD) misalignements on the focal plane on a simulation of the LSST mission {cite}`LSST2009`.

```{figure} ../../_static/psf-misalignments.png
---
height: 400px
name: psf-misalignments
---
Simulated focal plane of LSST. We used the CCD assembly/fabrication specification in Table 1 to generate the LSST focal plane tiled by 189 CCDs. Credit: {cite}`jee2011`.

```

- __Optical system__
    - _Scattered light_
    
    It consist of spuriours reflections within the optical system and the detector. An example for the HST mission can be found in Fig 3 in {cite}`krist1995c`.


    - _Wavelength dependency_
    
    The optical system is composed by several elements where some of them can be non-ideal refractive elements. This means that they introdcuce a wavelength dependance variation.


    - _Obscurations_

    Depending on the optical system design it might require arms to sustain the camera or even superposing mirrors that block each other. These obscurations modify the shape of the PSF and vary depending on the source's angle of incidence. They are 3D structures that are projected on the 2D pupil plane. As the obscurations are projected into the pupil plane they vary as a function of the angle of incidence. 
    
    The obscurations of the pupil plane have a direct relation with the shape of the PSF, specially for space-based surveys where the PSFs are closer to the diffraction limit. The [Fraunhoffer approximation](https://en.wikipedia.org/wiki/Fraunhofer_diffraction) of diffraction is most of the time a valid approximation for astronomical telescopes. This approximation allows to relate the wavefront at the pupil plane and the observed PSF with the Fourier transform. The obscurations force a zero amplitude value for the wavefront at the obscured parts of the pupil plane. The Fourier transform of these zero values can be easily identified in diffraction-limited PSFs, being an important contributor to the PSF shape.


```{figure} ../../_static/psf-HST-obscurations.png
---
height: 200px
name: psf-HST-obscurations
---
Projected obscurations of the Hubble Space Telescope. Credit: {cite}`krist2011`.

```

- __Filters__
    - Passband
    
    The filters serve to select the wavelengths incoming to the detector. Ideally they would be a perfect band-pass filter, begin one at the desired wavelength range and zero on the other wavelengths. However, it is not possible to manufacture an ideal filter. A real one does not have an abrupt transition, meaning that there are out-of-band contributions. It is also non-flat, meanining that the passband is near the unity but it changes with the wavelength. See this [page](https://www.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/en/megapipe/docs/filt.html) to visualise some examples of filters. As mentioned, the observations are always polychromatic, meaning that they are integrated in wavelength in the passband of the filter being used. 


```{figure} ../../_static/psf-filters.png
---
height: 300px
name: psf-filters
---
MegaCam filter set transmission for broad band filters u, g, r, i and z. Credit: [CFHT](https://www.cfht.hawaii.edu/Instruments/Imaging/Megacam/specsinformation.html).

```


## Ground-based

- __Seeing__

    In astronomy, seeing refers to the degradation of the image of an astronomical object due to the Earth's atmosphere. It is measured using three common descriptors: i) the Full Width Half Maximum (FWHM) of the PSF, ii) the Fried parameter $r_0$ and the atmospheric time constant $t_0$, and iii) the profile of the turblence strength as a function of the altitude $C_{N}^{2}$. The Fried parameter is a measure of the quality of optical transmission through the atmosphere due to random inhomogeneities in the atmosphere's refractive index.
    In terms of FWHM, if the seeing is above $1.5$ arcsec, the observations are practically unusable for weak-lensing purposes. The best sites on Earth can reach up to $0.4$ arcsec.


- __Atmosphere__

    The atmosphere plays a central role in ground-based observations. The refractive index of the atmosphere varies rapidly with the position generating different optical paths for the incoming light. The atmosphere presents different properties as we change altitude $h$ making it harder to model. Some of these properties are the turbulence strength $C_{N}^{2}(h)$, and the wind speed and diretion. The quality of the observations depend strongly on the exposure time used as well as the telescope location. For example, the best conditions are found in places like the [Mauna Kea observatory](https://en.wikipedia.org/wiki/Mauna_Kea_Observatories) in Hawaii. Most of the atmospheric simulations are simulated using parametric functions of the power spectrum. For example, in {cite}`jee2011` they simulate the atmosphere for the Legacy Survey of Space and Time (LSST) from the Vera C. Rubin Observatory by using several *phase screens* at different altitudes. Each phase screen describes a part of the atmosphere at a given altitude and how it modifies the incoming wavefront on its path towards the telescope. Each screen is characterised by a power spectrum like a Kolmogorov/Von Kármán model:
    
    $$
    \Psi(\nu) = 0.023 r_{0}^{-5/3} \left( \nu^{2} + \frac{1}{L_{0}^{2}} \right)^{-11/6},
    $$
    
    where $\nu$, $r_{0}$, and $L_{0}$ are the two-dimensional frequency, the Fried parameter, and the outer scale, respectively. The outer scale $L_0$ is infinite for Kolmogorov screens and finite for Von Kármán screens. Once the layer is simulated they are moved with a fixed wind speed and direction that will be finally integrated with the exposure time. This type of modelling requires measurements of the different parameters at the telescope's location. To have a broad picture of their values, for the Cerro Pachón in Chile, the parameters would be $L_{0} = 25\text{m}$, $r_{0} = 0.16\text{m}$, and a wind speed of at most $\sim 20 \text{m/s}$ at some random direction.
    
    Another way to simulate the atmospheric contribution to the PSF is to model the ellipticity contributions to the PSF by the atmosphere. This approach was studied by {cite}`heymans2012` where the authors study the ellipticity residuals of the observed stars at the [Canada-France-Hawaii Telescope](https://www.cfht.hawaii.edu) at the Mauna Kea observatory. They use the Von Kármán power spectrum and they found the best-fitting outer scale of their observations at different exposure times.


```{figure} ../../_static/psf-atmospheric-screen.png
---
height: 300px
name: psf-atmospheric-screen
---
Six layers of Kolmogorov/von Karman phase screens used for the atmospheric turbulence model. These phase screens represent the variations of the refractive index for different heights in the atmosphere. Credit: {cite}`jee2011`.

```

```{figure} ../../_static/psf-atmosphere-movie.gif
---
height: 300px
name: psf-atmosphere-movie
---
Variations of the PSF in short exposures due to the atmospheric turbulence. Credit: [url](http://userpages.irap.omp.eu/~jprieur/pisco-fr/pisco/figs/a8035_movie.gif)

```

- __Observing environment__

    The temperature differences in the telescope environment as well as the wind speed and direction on the surroundings of the telescope can affect its image quality. See {cite}`salmon2009` for a study on the Canada-France-Hawaii Telescope (CFHT).
    
```{figure} ../../_static/psf-dome-seeing.png
---
height: 300px
name: psf-dome-seeing
---
Frame of the [video](https://www.youtube.com/watch?v=HU1i6JzvIzY) that shows a Giant Magellan Telescope's simulation of refractive index variations as a function of temperature and wind speed and direction.

```    
    

## Space-based

- __Guiding errors__

    The satellite should remain perfectly still during an exposure. This is not the case and there exist a pointing error making the exposure the integration of the varyign satellite pointing. It sometimes referred as _Jitter_ or _Attitude and Orbit Control System_.
    
- __Thermal variations__

    The satellite experiences time where the sun is closer or were it is eclipsed by other object. This can occasionate high temperature changes in the space telescope. These temperature variations dilate and contract the optical system making it change of state as a function of temperature. It is sometimes to as _telescope's breathing_ for its repetitive pattern due to the orbits. See {cite}`nino2007` for an HST study of temperature variations.

- __Polarisation__

    Starlight can be naturally polarised by galactic foreground dust. The different polarisations that the incoming light has can interact differently with refractive elements of the optical system. This occasionates variations that are polarisation dependent. This source is currently being studied. 


## Detector level


- __Undersampling and pixelation__

    Many detectors, specially space-based ones, are undersampled or not Nyquist sampled. Generally, several exposures of the same object with small shifts are taken in order to super-resolve the object. The pixelation effect, the fact of using a limited number of pixels also affects the PSF and will impact the shear measurements. See {cite}`high2007` for a study of pixelation effects in weak lensing. See Section 3.5 and Figure 4 from {cite}`krist2011` for an analysis of these effects on the HST telescope.
 
```{figure} ../../_static/psf-pixelation.png
---
height: 300px
name: psf-pixelation
---
On top, the computed 336 nm HST PSF prior to pixellation. Below it is the PSF centered at the middle of a pixel and in the corner, integrated over the WFPC2 WF pixel area, shown at the same spatial scale. Credit: {cite}`krist2011`.

```  


- __Charge Diffusion Effect__

    There is a charge diffusion of the electrons between the pixels. It depends on the depth of the substrate and on the wavelength. It varies in the field of view as seen in {cite}`krist2003` on a study for the HST mission. It can be modelled as a varying convolutional kernel.
    
```{figure} ../../_static/psf-charge-difussion-effects.png
---
height: 200px
name: psf-charge-difussion-effects
---
Surface fits to the measured WFC charge diffusion blur kernel widths shown over the entire field of view (WFC1 & WFC2 butted together). The images are scaled to the same linear range. Credit {cite}`krist2003`.

```     
 
- __Charge Transfer Inefficiency__

    This phenomenon describes the inefficiency of transfering the charge when reading CCD detectors. It can be caused by charged particle radiation damage in space-based detectors. See {cite}`rhodes2010` and {cite}`massey2009`for studies of this phenomenon.

- __Brighter Fatter Effect__

    Each pixel in an camera is not independent of each other. One charge starts accumulating it modifies boundary pixel's electric fields. This occasionates a variation of the PSF size as a function of the flux and the wavelength. See {cite}`guyonnet2015` for a study and a model of the effect.

- __Quantum efficiency__
    This effect describes the ratio of created electrons from the number of incoming photons. It depends on the wavelength and on the detector's technology.
    
- __Other effects__
  - Analog-to-Digital Unit non-linearity
  - Thermal noise
  - Background estimation and subtraction

