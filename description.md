<!--
Project Description: Describe the activities to be undertaken in up to 7 pages
for Phase I proposals and up to 15 pages for Phase II proposals. See Section
II. Program Description, in this solicitation for guidance.
-->

# Context of OSE

<!--
Look at this proposal if we can: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2303681&HistoricalAwards=false
-->

<!--
In addition to requirements specified in the PAPPG, including a separate
section labeled "Broader Impacts", both Phase I and Phase II proposals must
have a separate section titled "Context of OSE" describing the context and
vision of the proposed OSE. This required section must include a description of
the guiding principles and long-term vision for the proposed OSE, the specific
societal or national need(s) that the OSE will address, and the anticipated
broader impacts of the OSE.
-->

<!--
In addition to requirements specified in the PAPPG, including a separate section labeled "Broader Impacts", both Phase I and Phase II proposals must have a separate section titled "Context of OSE" describing the context and vision of the proposed OSE. This required section must include a description of the guiding principles and long-term vision for the proposed OSE, the specific societal or national need(s) that the OSE will address, and the anticipated broader impacts of the OSE. 
-->

## Motivation

<!--
Why? Big python user base, need for stats tools in native python

* Python has large user base in general, especially in data science
   * TODO: stats to back up
* Many students now learning python
   * TODO: stats to back this up
* Lots of ML packages in python (pytorch/tensorflow, scikit-learn, …)
* Many domain sciences have toolboxes in Python (TODO: examples – astro, climate change, medical imaging, …)
   * Medical imaging https://monai.io/
* Stats community has historically done a lot of development in R, but has only sporadic python development
* Statisticians are more and more releasing python packages, but there is currently little support to go from research implementation to OSE


* List of examples of stats packages in python (TODO: add a bunch)
   *  https://scikit-survival.readthedocs.io/en/stable/install.html
   * Bin Yu has a bunch: https://www.stat.berkeley.edu/~yugroup/code.html
   * https://www.statsmodels.org/stable/index.html
   * https://docs.scipy.org/doc/scipy/reference/stats.html
   * https://lifelines.readthedocs.io/en/latest/
   * https://pingouin-stats.org/build/html/index.html

* List of stats methods missing/undersupported in Python
   * TODO: examples
-->

Generalized linear models (GLMs) play a central role in much of the statistics employed by scientific researchers, including fields as wide as neuroimaging, biology, chemistry, astronomy, and epidemiology.

Over the past decade, Python has become the de-facto tool for computational research.
Yet, for some applications in statistics, there are still gaps in its ecosystem, resulting in researchers having to use multiple computational platforms for their work.

Packages like `statsmodels` and `scipy.stats` cover much of the needed GLM functionality, but up until now there was no sophisticated GLM implementation that covered more advanced use cases.
Sponsored by the NSF (grant-XXXX), Iain Carmichael, in 20XX, implemented YAGLM: a modern, comprehensive, and flexible Python package for fitting and tuning penalized generalized linear models and other supervised M-estimators in Python.
YAGLM has great potential to strengthen the statistical ecosystem for Python, but much remains to be done before that can happen.

We propose bringing together domain researchers, developers, statisticians, and Python community managers to explore what an ideal class of generalized linear model implementations would look like.
We will use yaglm as a nucleus around which to form an Open Source Ecosystem.
This Ecosystem which will support the extension, maintenance, and governance of the yaglm, as well as provide a structure with which other projects can connect, or be incorporated into, to form a stable, comprehensive class of solutions that address advanced GLM-related needs.
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

## Where we (PIs) are starting OSE development (Where we are?)

* PIs are established in scientific python / statistics / communities
* Well positioned to lead community building effort


Our team is uniquely positioned for creating a community around this project:

- Jonathan Taylor and Jarrod Millman were founding members of the statsmodels project.
- Jarrod Millman and Stéfan van der Walt have been contributors to, and community maintainers in, the scientific Python community for close to two decades.
  Together, the started the Scientific Python project, that helps coordinate a large community of developers.
  Jarrod helped found scikit-learn, a highly successful machine learning library in Python.
- Iain Carmichael wrote YAGLM, the product that forms the core of this exploration.
- Jonathan Taylor, in collaboration with Trevor Hastie, is working on producing fundamental educational material surrounding generalized linear models.

### YaGLM

See \cite{carmichael2021yaglm}.

### ISLP


### resampling-with


## Long term vision

* Community meetings (training, governance)


### Societal or national needs: 

* statistical models underpin scientific research, a domain for all science

### Guiding principles

* Community based governance
  * Scientific Python-style governance
* Mimic orgs like scipy-hep, pangeo, astropy other domain stacks, a stack for statistics (bioconductor)

# Ecosystem Discovery

<!--
Include a plan for developing a strategy that: (1) describes methods to
evaluate and justify the need for the innovation within the current
technological landscape; (2) explains why an OSE is the right approach to
further develop the technology; and (3) outlines methods to identify potential
users who will utilize this technology.
-->

# Organization and Governance

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

# Community Building

<!--
Describe the specific activities to engage potential users and intellectual
content developers, including: (1) identification of the specific research and
development capabilities required of the potential contributor communities; and
(2) mechanisms to engage these communities (e.g., workshops, hackathons,
competitions, research coordination networks, and Ideas Labs).
-->

# Intellectual Merit

<!--
The Intellectual Merit criterion encompasses the potential to advance knowledge;
-->

# Results from Prior NSF Support

# Broader Impacts

<!--
The Broader Impacts criterion encompasses the potential to benefit society and
contribute to the achievement of specific, desired societal outcomes.
-->

<!--
Broader impacts may be accomplished through the research itself, through the activities that are directly related to specific research projects, or through activities that are supported by, but are complementary to, the project. NSF values the advancement of scientific knowledge and activities that contribute to achievement of societally relevant outcomes. Such outcomes include, but are not limited to: full participation of women, persons with disabilities, and other underrepresented groups in science, technology, engineering, and mathematics (STEM); improved STEM education and educator development at any level; increased public scientific literacy and public engagement with science and technology; improved well-being of individuals in society; development of a diverse, globally competitive STEM workforce; increased partnerships between academia, industry, and others; improved national security; increased economic competitiveness of the United States; and enhanced infrastructure for research and education.
-->

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
