Generalized linear models (GLMs) play a central role in much of the statistics employed by scientific researchers, including fields as wide as neuroimaging, biology, chemistry, astronomy, and epidemiology.

Over the past decade, Python has become the de-facto tool for computational research.
Yet, for some applications in statistics, there are still gaps in its ecosystem, resulting in researchers having to use multiple computational platforms for their work.

Packages like `statsmodels` and `scipy.stats` cover much of the needed GLM functionality, but up until now there was no sophisticated GLM implementation that covered more advanced use cases.
Sponsored by the NSF (grant-XXXX), Iain Carmichael, in 20XX, implemented YAGLM: a modern, comprehensive, and flexible Python package for fitting and tuning penalized generalized linear models and other supervised M-estimators in Python.
YAGLM has great potential to strengthen the statistical ecosystem for Python, but much remains to be done before that can happen.

We propose bringing together domain researchers, developers, statisticians, and Python community managers to explore what an ideal class of generalized linear model implementations would look like.
We will use YAGLM (hereforth: the product) as a nucleus around which to form an Open Source Ecosystem.
This Ecosystem which will support the extension, maintenance, and governance of the product, as well as provide a structure with which other projects can connect, or be incorporated into, to form a stable, comprehensive class of solutions that address advanced GLM-related needs.
We also propose educating new researchers on the theoretical principles of GLMs, so that they may better be able to apply these techniques to their work, and also participate actively in the Ecosystem. Specific goals will be to:

(1) Identify a wide array of use-cases for a Python GLM implementation,
    and the associated requirements.
(2) In response, explore ideal Application Programming Interface (APIs) for such an implementation.
(3) Ensure that adequate resources exist for coordinating work on the project.
(4) Establish clear guidelines for product governance collaboration.
(4) Create educational resources to widen community involvement in the project.

While this proposal will not fund the implementation of the above, it
may reasonably expected that members of the OSE will implement parts
of it as guidelines are established.

Our team is uniquely positioned for creating a community around this project:

- Jonathan Taylor and Jarrod Millman were founding members of the statsmodels project.
- Jarrod Millman and Stéfan van der Walt have been contributors to, and community maintainers in, the scientific Python community for close to two decades.
  Together, the started the Scientific Python project, that helps coordinate a large community of developers.
  Jarrod helped found scikit-learn, a highly successful machine learning library in Python.
- Iain Carmichael wrote YAGLM, the product that forms the core of this exploration.
- Jonathan Taylor, in collaboration with Trevor Hastie, is working on producing fundamental educational material surrounding generalized linear models.
