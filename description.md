<!--
Project Description: Describe the activities to be undertaken in up to 7 pages
for Phase I proposals and up to 15 pages for Phase II proposals. See Section
II. Program Description, in this solicitation for guidance.
-->

<!--
Look at this proposal if we can: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2303681&HistoricalAwards=false
-->

# Overview

The Python software ecosystem has been embraced by numerous scientific domains.
This often involves transitioning or rewriting well established existing computational platforms (see, e.g., astronomy moving away from IDL).
The benefits of doing so, are that researchers get access to a wide array of computational libraries, developed using stringent software engineering methodology and principles.
Students and young researchers often receive training in Python development, and researchers have access to a large community of practitioners and developers ...
As promising as the above is, there is a glaring hole in the ecosystem when it comes to statistics functionality.
This may well be exacerbated by the fact that there is a well functioning computational ecosystem, namely R, that focuses specifically on this sub-domain.
This means that statisticians, instead of contributing their work to multiple ecosystems, typically only contribute to R.
We believe that there is benefit to involving statisticians in improving and expanding the offering of the Python ecosystem, where the pervasive software engineering disciplines, such as comprehensive testing, continuous integration, etc. will strengthen the offering further.

We envision an Open Source Ecosystem for Statistics in Python that coordinates, provides a community of practice, and acts as a gathering place for statisticians and researchers that want to disseminate their work in Python.
To create such an ecosystem requires narrowing our focus to an example that will provide the necessary practical learning opportunity.
For this purpose, we have identified two open source Python packages to serve as pilot projects and anchor the OSE:

- `YAGLM` \cite{carmichael2021yaglm}: a library for generalized statistical models (GLM) in Python.
- `ISPL` 

Using `YAGLM` and `ISPL` as pilot projects, we will investigate the typical challenges of bringing an existing package, developed by researchers, into the Python software ecosystem.
We will build a community of statisticians and researchers that give input on what an ideal GLM implementation should look like in Python.
This same community could eventually help explore the wider statistical space.
We will connect with existing OSEs (of which several exist in scientific Python), to learn more about successful governance, social, and technical practices.
We will distill these ideas into documents that are of benefit to other OSEs, but also to our own.
Finally, we will build governance, testing, and contributor scaffolding around the example product, with an eye towards learning how the same can be done for other statistical packages.

In order to support the statistical ecosystem, we need to widen participation in the developer community.
One way to involve the next generation, as well as those without previous access to such communities, is to provide statistical training of the concepts involved.
Again, using the product as a catalyst, we will present workshops that combine theoretical and practical software training around GLMs, to create a pathway towards contributing to the statistical OSE.

Our overarching goal is to start with a product, but to move to a class of products.
To form a small OSE around an example concept, but to generalize that OSE to enable a larger scale transformation of the statistical Python ecosystem, to where statisticians and researchers, experienced and newly trained, contribute to a diverse, vibrant collection of open source packages that turn Python into a highly viable, desirable computational platform of choice for statistics.

# Context of OSE

<!--
In addition to requirements specified in the PAPPG, including a separate
section labeled "Broader Impacts", both Phase I and Phase II proposals must
have a separate section titled "Context of OSE" describing the context and
vision of the proposed OSE. This required section must include a description of
the guiding principles and long-term vision for the proposed OSE, the specific
societal or national need(s) that the OSE will address, and the anticipated
broader impacts of the OSE.
-->


## Scientific Python

![Scientific Python Ecosystem](./figures/ose-ecosystem.pdf)

The entire space of Python libraries for scientific computation is most often referred to as the scientific Python ecosystem.
Inside it, there exist several OSE-like organizations.
Notable examples include The Scientific Python Project, scikit-HEP (high energy physics), pangeo (earth sciences), astropy (astronomy), and nipy (neuroimaging).
The first of these, founded by PIs SJvdW and KJM, aims to better coordinate the development of scientific Python projects as well as their associated communities of contributors.
The others are domain-specific communities that foster the development of libraries and infrastructure that address field-specific concerns.

We envision that the proposed OSE, similarly, will become a community-owned structure that provides operational and governance guidelines, and that supports the organization of, contribution to, and sustainance of computational libraries.
However, instead of being specific to any *domain*, it will focus on *statistical methods* as a whole.
While the boundaries of the OSE are yet to be established, it may, for example, provide technical and community guidance, host technique-specific or software engineering knowledge, or provide shared infrastructure.

Scientific Python is characterized by several larger, well-established libraries that have coalesced from smaller, experimental packages.
While smaller packages are developed relatively freely, large libraries have a strong focus on best-in-class software engineering, such as testing and continuous integration.
In addition, the emphasize best practices of collaboration, such as community-driven governance and decision making, documentation, and newcomer onboarding.
We foresee that the OSE will act as point of coagulation, by which important functionality that benefit many researchers is identified and incorporated into existing libraries.
In addition, the OSE will distribute knowledge on best practices to smaller projects, offering a transition pathway for expanding the offering of high-quality algorithm implementations to researchers.
Distributing and assisting with the adoption of such knowledge further democratizes the contribution landscape, and expands the community of participating researcher-developers.

<!--
Proposals must also have (1) a pointer to the existing publicly-available
open-source product that is being transitioned; (2) details on the current
status of the open-source product, development model, methods of dissemination,
and user base; (3) a description of the problem being addressed, and the
novelty of the intended product being transitioned, including substantiating
evidence of the technology's potential to significantly impact/address the
problem; and (4) a strong justification that makes the case that the team is
qualified to conduct this work.
-->

## Statistics

Through `CRAN`, the `R` community has been successful in enabling publication of many and varied
software packages for statistical analysis. The packages vary widely in terms of adherence to best practices
in software engineering, ranging from professional level (e.g. the tidy-verse package `tidyr`) to
course projects from Master's or PhD courses. One of the successes of `CRAN` is that it broadly facilitates
distribution of packages, although there is little oversight of how these packages are related.
Certain subcommunities, such as tidy-verse and BioconductoR, do have governance models, and guidelines on how packages should related to one another, be released, how quality standards are enforced, etc.

In contrast to `R`, the statistical software environment in Python is most recognizable as larger foundational data-structure and algorithmic
libraries such as `scipy`, `pandas`, and `scikit-learn`. By and large, these well-established statistical software libraries
adhere to best practices in software development.
Other than publishing to the central, general Python Packaging Index, there is no coordinating mechanism similar to `CRAN` for loosely organizing
small or experimental packages in Python into applicable, domain- or method-specific "stacks".

The proposed OSE provides a "best of both worlds" solution: a place where statistical packages for scientific Python can be explored and developed, while distributing knowledge on software engineering methodology to their developers and to statisticians at large.
This knowledge could be beneficial also to those developing libraries for R, resulting in the cross-pollination of modern software engineering and healthy community practices.

## Pilot Projects

### `YAGLM`

The `YAGLM` open-source Python package (https://github.com/yaglm/yaglm) was developed to make the framework of modern GLM
methodology (various loss function, regularizer, solvers) available and easily accessible to data analysts \cite{
yaglm2021carmichael}. Beyond the basic lasso/ridge,
the package supports structured penalties such as the nuclear norm as
well as the group, exclusive, fused, and generalized lasso and non-convex but linearizable
penalties. `YAGLM` comes with a variety
of tuning parameter selection methods including: cross-validation,
information criteria that have favorable model selection properties,
and degrees of freedom estimators.

Standard statistical software design patterns had to be rethought in
order to handle the breadth of the GLM framework. For example,
scikit-learn’s API and estimator object backend [TODO: CITATIONS] have
become a frequently used template for developing statistical and
machine learning software [TODO: perhaps some citations
e.g. celer]. Initial attempts at extending scikit-learn quickly
revealed different backend and frontend API design choices would need
to be made. Some of these design choices (e.g. config objects to
specify models or a separate solver object class for the optimization
algorithm) will be useful for other statistical software packages.

The initial development of `YAGLM` was done in short bursts by a few
core developers. It is currently available on github and has a few
users. `YAGLM` is missing important engineering details like continuous
integration, extensive testing, and quality documentation. It is also
missing community support like governance, developer onboarding and a
code of conduct.

### ISLP

Ths `ISLP` open-source Python package (https://github.com/intro-stat-learning/ISLP) is written to accompany an introductory text on statistical learning and `python`,
closely following the examples in the hugely successful `R` version. Besides just providing labs,
it provides pythonic design matrix building, a simple implementation of Bayesian Additive Regression Trees
and object oriented stepwise model selection. Planned development include extending the `pygam` package;
regularized regression specification (to be used by `yagml`); integration of a `python` version
of the very popular `glmnet` package in `R`.

The corresponding textbook was published in July.  The project aims to
use good (if not best) software engineering practices.  It is expected
that it will be used in several introductory data science and
statistics courses nationwide which will serve as a test of the robustness
of these practices, evidenced by the responsiveness to (GitHub) and other issues that arise.


## Team

Our team are well established in the statistics and scientific Python
communities. We are uniquely positioned for creating a community around
this OSE:\

**Stéfan van der Walt** is a research scientist at UC Berkeley. He is the founder
of scikit-image and co-author of Elegant SciPy.
He regularly teaches Python at bootcamps, campus courses, and at the
annual G-Node Advanced Scientific Programming in Python summer schools.
He contributes to numerous packages in the ecosystem
including NumPy, SciPy, DiPy, IPython, scikit-learn, scikit-image, and NetworkX.
He is the software architect of the Cesium machine-learning library and web platform, and
released several research software libraries, such as SupReMe for
super-resolution imaging, and DPT for calculating Discrete Pulse Transforms.
Stéfan is a director of NumFOCUS, and serves on the steering committees of NumPy, SciPy, and the
PSF's Scientific Working Group. He cofounded the Scientific Python project in 2020 with Jarrod Millman.

**Jarrod Millman** is a senior open source scientific Python developer at UC
Berkeley. He cofounded the Neuroimaging in Python project.
He was the NumPy and SciPy release manager from 2007 to 2009.
He was on the SciPy steering committee from
2007 to 2010.  He was the SciPy conference chair from 2008 to 2011 and the
SciPy India conference chair from 2009 to 2012. He cofounded NumFOCUS and
served on its board from 2011 to 2015.  Currently, he is the release manager of
NetworkX, scikit-image, pygraphviz, numpydoc, and a few other packages. He
cofounded the Scientific Python project in 2020 with Stéfan van der Walt.

**Iain Carmichael** is an assistant professor of statistics at UC Berkeley.
His research focuses on developing statistical/machine learning algorithms for data with
a complex structure such as networks, images, and multi-view/modal data. 
He wrote `YAGLM`, the product that forms the core of this exploration.

**Jonathan Taylor** is a professor of statistics at Stanford University and is recognized
both in the academic statistics community and the scientific `python` community. His research focuses
on selective inference and signal detection in structured noise.
He has been involved in the scientific python community for many years, including
early work on `statsmodels`, `nipy` among others.
As part of this, he has learned some of the best practices from the scientific `python` world.
He also works closely with statisticians in the `R` community. 
In collaboration with Trevor Hastie, he is the main developer on `ISLP` a package bridging
the `R` and `python` worlds in that it provides `python` support for course material in a
hugely successful `R` book: "Introduction to Statistical Learning with Applications in R".

**Matt Haberland** is assistant professor of the bioResource and agricultural engineering at
California Polytechnic State University. He is the maintainer of `scipy.stats`, which
provides a large number of probability distributions, summary and frequency statistics,
correlation functions and statistical tests, masked statistics, kernel density estimation,
quasi-Monte Carlo functionality, and more.

## Long term vision

As described above, the current state of open source statistical software is mixed. The `R` community
has many individual or small group contributors, though many lack proper training in best practices for open source software. In the
`python` community, at least as represented by the larger packages, is represented by larger, well-organized
groups with clear governance practices.

This proposal aims to bridge these two worlds: it is unreasonable to assume statisticians trained in
cutting-edge methodology to simultaneously master best practices in software engineering. Similarly,
software engineers are not trained at the cutting edge of statistical methodology. However, there is certainly
a middle ground: graduate students in statistics can be trained in good (i.e. not as extensively as required
for "best") practices in software engineering. Similarly, those with strong software engineering skills
can learn what are the types of APIs required to implement cutting edge methodology in software. 

In colonizing this middle ground, we hope to achieve several goals.

1. Better software engineering practices for academically trained statisticians writing software both in `R` and `python`.

2. Establishment of new, well-engineered and robust APIs (building on the
success of `sklearn`'s simple but powerful API) for implementation of cutting-edge statistical
methodology in different modeling paradigms.

3. Cross-pollination between `R` and `python` statistical software communities. The current state sees
`R` with mostly small development groups with `python` leaning towards larger groups. Meeting in this middle
ground will necessitate communication between the groups.

### Societal or national needs:

* statistical models underpin scientific research, a domain for all science

### Guiding principles

* Community based governance
  * Scientific Python-style governance
* Mimic orgs like scipy-hep, pangeo, astropy other domain stacks, a stack for statistics (bioconductor)

# Program of Work

## Pilot Projects

 `YAGLM` and `ISLP`

Stefan and Jarrod will work with Iain to see what is needed to add the missing engineering and practices.

Specific goals will be to:

(1) Identify a wide array of use-cases for a Python GLM implementation,
    and the associated requirements.
(2) In response, explore ideal Application Programming Interface (APIs) for such an implementation.
(3) Ensure that adequate resources exist for coordinating work on the project.
(4) Establish clear guidelines for product governance collaboration.
(4) Create educational resources to widen community involvement in the project.

While this proposal will not fund the implementation of the above, it
may reasonably expected that members of the OSE will implement parts
of it as guidelines are established.

## Scientific Python Domain Stacks

## Bioconductor and Tidyverse

## Ecosystem Discovery

<!--
Include a plan for developing a strategy that: (1) describes methods to
evaluate and justify the need for the innovation within the current
technological landscape; (2) explains why an OSE is the right approach to
further develop the technology; and (3) outlines methods to identify potential
users who will utilize this technology.
-->

The project team will organize 10 workshops---seven in-person and two hybrid.

To inform those workshops, we will create surveys.

## Organization and Governance

<!--
Describe specific activities and their rationale that will identify: (1) the
appropriate organizational, coordination, and governance models including the
licensing approach to be employed; (2) the specific continuous development and
integration processes and infrastructure that is most suitable for open,
asynchronous, and distributed development of the open-source product, (3)
processes for ensuring quality, security, privacy or ethical concerns of new
content; and (4) the best methods for sustaining the organizational structure,
including metrics to assess and evaluate long-term success of the development
methodology, support for users, and on-boarding mechanisms for new
contributors.
-->

## Community Building

<!--
Describe the specific activities to engage potential users and intellectual
content developers, including: (1) identification of the specific research and
development capabilities required of the potential contributor communities; and
(2) mechanisms to engage these communities (e.g., workshops, hackathons,
competitions, research coordination networks, and Ideas Labs).
-->

## Project Timeline and Workshop Overview

The first three workshops will be held within the first quarter of the funding cycle.
The next four workshops will be held during the second and third quarters.
The final three workshops will be held during the final quarter.
Each in-person workshop is expected to include up to 20 people and
the virtual workshops will include up to 30 people.

**Workshop 1:** yaglm

**Workshop 2:** islp

**Workshop 3:** statitisticians working in Python

**Workshops 4, 5, 6:** graduate students / postdocs (stanford)

**Workshop 7:** teachers

**Workshop 8 (virtual):** yaglm

**Workshop 9 (virtual):** islp

**Workshop 10:** final plan


# Intellectual Merit

<!--
The Intellectual Merit criterion encompasses the potential to advance knowledge;
-->

This proposal addresses two gaps in the statistical software ecosystem. On the one hand,
there  are many small groups or individual developers of statistical packages who lack the training
in best (or better) practices in software engineering needed for open source an project to survive. On the other hand,
the scientific python community adheres closely to such projects, resulting in well-engineered software
packages such as `numpy`, `scipy`, `pandas` and `sklearn`. This proposal seeks to learn and document how to bridge this gap, starting with `yagml` as a pilot project. With this knowledge, the OSE will be able to propagate this model
for other projects, resulting in better engineered software in the statistical community.

The context of statistical software today is such that the `R` developer community consists of many
individual or small groups, while the scientific `python` core projects and domain stacks are closer to the
software engineering models. As a byproduct, any build between small and well-engineered will necessitate
a bridge between `R` and the scientific `python` community. Learning what works best in each development community
and what common ground exists in the two developer communities is expected to build stable parts of this
bridge between the two developer communities.

# Broader Impacts

<!--
The Broader Impacts criterion encompasses the potential to benefit society and
contribute to the achievement of specific, desired societal outcomes.
-->

<!--
Broader impacts may be accomplished through the research itself, through the activities that are directly related to specific research projects, or through activities that are supported by, but are complementary to, the project. NSF values the advancement of scientific knowledge and activities that contribute to achievement of societally relevant outcomes. Such outcomes include, but are not limited to: full participation of women, persons with disabilities, and other underrepresented groups in science, technology, engineering, and mathematics (STEM); improved STEM education and educator development at any level; increased public scientific literacy and public engagement with science and technology; improved well-being of individuals in society; development of a diverse, globally competitive STEM workforce; increased partnerships between academia, industry, and others; improved national security; increased economic competitiveness of the United States; and enhanced infrastructure for research and education.
-->

# Results from Prior NSF Support

<!--

Phase I proposals will be evaluated on the basis of the following solicitation-specific review criteria:

- Does the proposal present a convincing case that the OSE will address an issue of significant societal or national importance that is not currently being adequately addressed?
- Does the proposal clearly describe the long-term vision for the OSE, including potential partnerships and sustainability?
- Does the proposal provide convincing evidence that a substantial user base exists, or could be built, for the open-source product that will be the subject of the OSE?
- Does the proposal justify the OSE within the current technological landscape and present a strong case that an OSE is the best approach for generating impact?
- Does the proposal present clear plans for discovering the ecosystem within which the OSE will be operating?
- Does the proposal present a credible plan for exploring the establishment of a sustainable organizational structure?
- Does the proposal present a credible plan to develop a strategy for building a community of contributors?
- Does the proposing team have the required expertise and experience to undertake the Phase I activities described in the solicitation?
- Will NSF support serve as a critical catalyst for the establishment of the OSE?
- Does the proposal include third-party letters of collaboration from current users of the open-source product that is the subject of the OSE?

-->
