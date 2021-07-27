# Introduction to PSF validation

Once the PSF has been modelled, it is important to have tools to evaluate the accuracy of the model, and how much bias it may introduce in the weak lensing analysis.

As the PSF can only be measured on stars, a small sample of stars is usually reserved for the validation and are not used in fitting the model ; typically 20% of the stars are used for validation.

Evaluating the PSF is most of the time done by measuring its shape. This can be done in a variety objects but usually involves moments-based method, which are described in (insert link here). The two main measures that are used are the size, defined as $T = I_{11} + I_{22}$ (where I represents the second moments), and the ellipticity $e$, defined as in (link to the right section).

The process involves to compute the modelled PSF at the location of the reserved stars, measure its shape parameters, measure the shape parameters of the real PSF, and compare the two ; we define here the residual ellipticity $\delta e_\text{PSF} = e_\text{PSF} - e_\text{model}$ and the residual size $\delta T_\text{PSF} = T_\text{PSF} - T_\text{model}$.

Most of the time, you will want to have some kind of objective measure of the accuracy of the model, for instance how much bias is introduced in your final product by the PSF model, so as to set a threshold for when the model is acceptable. You also want a way to identify what the issues with your current model are.

A first way to do this is to simply look at the distribution of the residual quantities. This is done for instance in figure 8 of {cite}`Bosch_2017` which is reproduced here. They chose to compute the residuals both for the reserved stars and for the stars on which the PSF was fitted, as well as on coadded PSF (you can find more details about those in section 3.3.1 of the paper). 

```{figure} ../../_static/psf_validation_residuals.png
---
width: 800px
name: psf_validation_residuals
---
Distribution of the (fractionnal) ellipticity and size residuals for the HSC PSF modelisation. Credit: {cite}`Bosch_2017`.

```

One of the striking results is that the model is significantly better on the stars to which it was fitted than on the reserved stars, which implies that there may be some overfitting or some interpolation problem. The figure also highlights another issue of the PSF with an error depending on the seeing, and in particular being very high for good seeing, which was likely due to some issues with the software and for the initial guess for the PSF size which was too high.

The same paper also includes a plot of the residual quantities against the magnitude (figure 5) which you can see below. It reveals an unwanted dependence of the PSF model error on the magnitude of the stars, which is mostly due to the brighter-fatter effect ; the blue curve shows the result after correcting for this effect.
```{figure} ../../_static/psf_validation_brighter_fatter.png
---
width: 400px
name: psf_validation_brighter_fatter
---
Distribution of the (fractionnal) size residual for the HSC PSF modelisation according to magnitude. Credit: {cite}`Bosch_2017`.

```

The DES collaboration used a similar plot to show the (unmodelled) variation in PSF according to the color of the stars. They interpret the fact that the blue stars (in cyan) are larger than the red stars as the predominance of atmospheric distortion in chromatic effects (as the other chromatic effects tend to make redder stars larger).
```{figure} ../../_static/psf_validation_color.png
---
width: 400px
name: psf_validation_color
---
Distribution of the size residual for the DES PSF modelisation according to magnitude, separated by color. Credit: {cite}`Jarvis_2020`.

```


These are the main diagnostics for evaluating the PSF globally. Additionally, it can be a good idea to have a look at the error in PSF modelling on the focal plane, by reporting the error for each star according to its position on the focal plane of the instruments. This gives a figure like the following one which is once again extracted from the same paper.

```{figure} ../../_static/psf_validation_focal_plane.png
---
width: 400px
name: psf_validation_focal_plane
---
Distribution of the (fractionnal) ellipticity residual on the focal plane for HSC. Credit: {cite}`Bosch_2017`.

```

It is clear that part of the PSF variation is not modelled ; this can be due for instance due to interpolation using low-order polynomials, leaving the possibility for high-order variations to remain (however, fitting a polynomial of higher order requires many more stars, which is not always doable). DES collaborators ({cite}`Jarvis_2020`) also used this plot to identify the presence of tree ring patterns (circular patterns caused by imperfections in the manufacturing process).

While having a look at the focal plane can help quickly detecting unmodelled PSF variation, it remains a mostly qualitative measure. In order to evaluate more precisely the PSF and more specifically detect the presence of correlations in the PSF errors, as well as to estimate the bias caused by incorrect PSF modelling, the **rho statistics** have been introduced ; you will find an introduction to these diagnostic tools in the next section of this book.
