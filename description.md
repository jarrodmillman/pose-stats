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
For this purpose, we have identified YAGLM \cite{carmichael2021yaglm}: a library for generalized statistical models (GLM) in Python.

Using YAGLM as a pilot project, we will investigate the typical challenges of bringing an existing package, developed by researchers, into the Python software ecosystem.
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

## Context and vision

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

### Scientific Python

#### Scientific Python Ecosystem

core projects, engineering best practices,

#### Domain Stacks

astropy, scikit-hep, pangeo, nipy

### Statistics

#### R

#### Python

#### YAGLM

- details on the current status of the open-source product, development model, methods of dissemination,
and user base;

- missing engineering / community work (ci, tests, documentation, governance, onboarding, code of conduct, etc.)

#### ISLP

### Team

Our team is uniquely positioned for creating a community around this project:

- Stéfan van der Walt is the founder of scikit-image and co-author
  of Elegant SciPy. Stéfan led an early project to document NumPy and SciPy, and
  helped to construct
  the platform and tools that allowed the community to complete documentation via
  volunthttps://scientific-python.org/eer collaboration.
  He led the development of the scikits index.
  He mentored Google Summer of Code students from 2010 through 2015.
  He organized numerous Python-related events, and has served on the
  SciPy Conference organizing committee since 2009.  He served as
  conference co-chair, program committee chair, and proceedings
  co-chair, in which capacity he wrote and deployed, together with KJM, the
  current proceeding paper review and publication system.
  He regularly teaches Python at bootcamps, campus courses, and at the
  annual G-Node Advanced Scientific Programming in Python summer schools.
  He contributes to numerous packages in the ecosystem
  including NumPy, SciPy, DiPy, IPython, scikit-learn, and scikit-image.  He is the software
  architect of the Cesium machine-learning library and web platform, and
  released several research software libraries, such as SupReMe for
  super-resolution imaging, and DPT for calculating Discrete Pulse Transforms.
  Stéfan is a director of NumFOCUS, and serves on the steering committees of NumPy, SciPy, and the
  PSF's Scientific Working Group.
- Jarrod Millman is a senior open source scientific Python developer at UC
  Berkeley. He received a BA from Cornell University in 1998. After working at
  the Center for Neuroscience at UC Davis, he came to UC Berkeley in 2000—first
  to design the data analysis system for the Brain Imaging Center and then as the
  director of research computing for the Neuroscience Institute.  At Berkeley,
  Jarrod cofounded the Neuroimaging in Python project, which spawned the statsmodel
  project. He was the NumPy and SciPy release manager from 2007 to 2009.
  He was on the SciPy steering committee from
  2007 to 2010.  He was the SciPy conference chair from 2008 to 2011 and the
  SciPy India conference chair from 2009 to 2012. He cofounded NumFOCUS and
  served on its board from 2011 to 2015.  Currently, he is the release manager of
  NetworkX, scikit-image, pygraphviz, numpydoc, and a few other packages. He
  cofounded the Scientific Python project in 2020 with Stéfan van der Walt.
- Iain Carmichael wrote YAGLM, the product that forms the core of this exploration.
- Jonathan Taylor, in collaboration with Trevor Hastie, is working on producing
  fundamental educational material surrounding generalized linear models.

## Long term vision

* Community meetings (training, governance)

- better statistical software for Python developed by statisticians

- better software engineering and practices for statisticians

- improved software engineering and practices for R

### Societal or national needs: 

* statistical models underpin scientific research, a domain for all science

### Guiding principles

* Community based governance
  * Scientific Python-style governance
* Mimic orgs like scipy-hep, pangeo, astropy other domain stacks, a stack for statistics (bioconductor)

# Program of Work

## YAGLM (pilot project)

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

## Ecosystem Discovery

<!--
Include a plan for developing a strategy that: (1) describes methods to
evaluate and justify the need for the innovation within the current
technological landscape; (2) explains why an OSE is the right approach to
further develop the technology; and (3) outlines methods to identify potential
users who will utilize this technology.
-->

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

# Intellectual Merit

<!--
The Intellectual Merit criterion encompasses the potential to advance knowledge;
-->


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
