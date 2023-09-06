<!--
Project Description: Describe the activities to be undertaken in up to 7 pages
for Phase I proposals and up to 15 pages for Phase II proposals. See Section
II. Program Description, in this solicitation for guidance.
-->

<!--
Look at this proposal if we can: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2303681&HistoricalAwards=false
-->

# Overview

Python \cite{millman2011python} and `R` \cite{r2023r}
are the two most popular computational platforms for data science.
`R` is largely developed by statisticians, whereas scientific Python is mostly built by researchers from the applied sciences.
As a consequence, Python's statistical capabilities are lacking, and statisticians do not benefit from widespread use of their innovations on this popular platform.
The goal of this grant is to investigate the formation of an OSE that will foster the growth of statistical software, as well as its surrounding developer community, in Python.
<!-- Such an OSE, as a community of practice, will act as a bridge, connecting statisticians and researchers that wish to distribute implementations of statistical innovations in Python with library developers. -->
By widely disseminating lessons learned about statistical methodology, software engineering, sustainability, governance, and community management, the OSE will enrich its community of contributors.
A positive side-effect will be the cross-pollination of ideas between the `R` and Python platforms.

We envision an OSE that has the capacity to catalyze a large scale transformation of the statistical Python ecosystem, such that statisticians and researchers, experienced and newly trained, contribute to a diverse, vibrant collection of open source packages that turn Python into a highly viable computational platform for statistics in applied science and education.
We will use `YAGLM` \cite{yaglm-github} (an open-source library for penalized
generalized linear models \cite{carmichael2021yaglm}) and `ISLP`
\cite{islp-github} (an open-source library that provides functions and
datasets for the accompanying textbook *An Introduction to Statistical Learning:
with Applications in Python* \cite{james2023introduction}) as exemplar packages that typify
different research artifacts that may be found in the ecosystem, but that have
not matured to have built communities of governance and software development
around them.
We will investigating the challenges of bringing these packages,
developed by statisticians, fully into the Python software ecosystem.
These challenges include improving governance, testing, and contribution
scaffolding, with an eye toward learning how the same can be done for other
statistical packages.

The OSE will widen participation in the developer community and the OSE itself---especially by involving the next generation of researchers and developers, and those outside of existing contributor communities.
Such outreach will involve statistical and technical training, informed in part by the needs of the pilot projects and their developers.
Given our experience, and the experience of our colleagues in statistics departments across the nation, we believe there is a large demand for such an OSE.
Increasing numbers of students are entering our departments already familiar with scientific Python and wanting more training in it.
For example, a recent poll of UC Berkeley Statistics masters students and alumni found that the overwhelming majority wanted deeper training in Python statistical software.
Unfortunately much of the needed infrastructure is missing.
NSF support at this crucial junction in time would serve as a critical catalyst, providing resources to better understand the potential user and contributor community, and to design a Statistical Python OSE that would grow that community and support its needs.

An overarching goal of the OSE will be to extend what is learned from the pilot projects to the entire class of products that span statistical Python.
This will be achieved by building a community of statisticians, researchers, and students that give input on what an ideal statistical landscape should look like in Python;
connecting with existing OSEs, in both the Python and R worlds, to learn more about successful governance, social, and technical practices;
and distilling those ideas into documents that are of broad benefit to OSEs, including our own.


# Context of OSE

<!--
In addition . to requirements specified in the PAPPG, including a separate
section labeled "Broader Impacts", both Phase I and Phase II proposals must
have a separate section titled "Context of OSE" describing the context and
vision of the proposed OSE. This required section must include a description of
the guiding principles and long-term vision for the proposed OSE, the specific
societal or national need(s) that the OSE will address, and the anticipated
broader impacts of the OSE.
-->


## Scientific Python


The entire space of Python libraries for scientific computation is most often referred to as the scientific Python ecosystem \cite{perez2011python}.
Inside it, there exist several OSEs including Scientific Python, scikit-HEP (high energy physics) \cite{rodrigues2020syo}, pangeo (earth sciences), astropy (astronomy) \cite{price2018astropy}, and nipy (neuroimaging) \cite{millman2007analysis}.
The first of these aims to better coordinate the development of scientific Python projects as well as their associated communities of contributors.
The others are domain-specific communities that foster the development of libraries and infrastructure that address field-specific concerns.

<!--
\begin{wrapfigure}{r}{0.6\textwidth}
  \begin{center}
    \includegraphics[width=0.58\textwidth]{./figures/ose-ecosystem.pdf}
    \caption{The Statistical Python OSE will play a similar role to other domain-specific OSEs.}
  \end{center}
\end{wrapfigure}
-->
<!--
We envision that the proposed OSE, similarly, will become a community-owned structure that provides operational and governance guidelines, and that supports the organization of, contribution to, and sustenance of computational libraries.
-->
We will model the Statistical Python OSE on these existing domain-specific OSEs.
<!--
However, instead of being specific to a specific *domain*, it will focus on *statistical methods* as a whole.
-->
<!--
Remove following sentence and replace with expanding the above to explain the need for funding.
Other domain-specific OSE were funded by large science or specific grants, the individualized
work of statisticians necessitates a phase I scoping and phase II implementation to create a
self-sustaining community run organization supporting and growing the community of developers
and users of statistical Python.
-->
These OSEs were typically established as part of focused research grants or major scientific equipment grants.
Such a funding model does not lend itself well to a broad, methods-based field such as statistics.
While statistical methods are currently, by necessity, implemented as part of applied work, it makes sense to consider them in a more generalized context, allowing for implementations with wider reach.
Such an approach covers new terrain for scientific Python, so that it is prudent to first consult widely on *planning* what needs to be built, and how.
These activities would lay the groundwork for a self-sustaining, community-run organization around which a community of developers and users can coalesce.
<!--
That community will, in turn, implement the plan and help to support the resulting products.
-->

<!--
Scientific Python is characterized by several larger, well-established libraries that have coalesced from smaller, experimental packages.
While smaller packages are developed relatively freely, large libraries have a strong focus on best-in-class software engineering, such as testing and continuous integration.
In addition, the emphasize best practices of collaboration, such as community-driven governance and decision making, documentation, and newcomer onboarding.
We foresee that the OSE will act as point of coagulation, by which important functionality that benefit many researchers is identified and incorporated into existing libraries.
In addition, the OSE will distribute knowledge on best practices to smaller projects, offering a transition pathway for expanding the offering of high-quality algorithm implementations to researchers.
Distributing and assisting with the adoption of such knowledge further democratizes the contribution landscape, and expands the community of participating researcher-developers.
-->

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

## Statistical Software

Through `CRAN`, the `R` community has been successful in enabling publication of many and varied
software packages for statistical analysis. The packages differ widely in the degree to which they adhere to best practices
in software engineering, ranging from professional level to
course projects from Master's or PhD courses. One of the successes of `CRAN` is that it broadly facilitates
distribution of packages, although there is little oversight of how these packages are related.
Certain subcommunities, such as tidy-verse \cite{wickham2019welcome} and
Bioconductor \cite{gentleman2004bioconductor}, provide additional structure
and guidance to contributors and users in the form of governance models,
developer guidelines, testing infrastructure, and release management.

In contrast to `R`, the statistical software environment in Python is most recognizable as larger foundational data-structure and algorithmic
libraries such as NumPy \cite{harris2020array}, SciPy \cite{virtanen2020scipy}, pandas \cite{mckinney-proc-scipy-2010},
NetworkX \cite{hagberg2008}, scikit-image \cite{vanderwalt2014scikit}, and scikit-learn \cite{scikit-learn}. By and large, these well-established software libraries
adhere to best practices in software development \cite{millman2014developing}.
Other than publishing to the central, general Python Packaging Index, there is no coordinating mechanism similar to `CRAN` for loosely organizing
small or experimental packages in Python into applicable, domain- or method-specific "stacks".

The proposed OSE provides a place where statistical packages for scientific Python can be explored and developed, while distributing knowledge on software engineering methodology to their developers and to statisticians at large.
Shared knowledge and experiences will likely permeate across computational ecosystems, resulting in the cross-pollination of modern software engineering and healthy community practices.

## Pilot Projects

We selected two pilot projects to inform the needs of an OSE in statistical Python.
They are intentionally at different phases of maturity and have different emphases.
The first aims to provided data science practitioners with state of the art algorithms for generalized linear models; the second aims to educate students and researchers on foundational statistical methods.
By examining the needs of the developer and user communities of these two packages, we aim to learn not only what functionality is missing, but also how community, onboarding, and engineering practices can be improved.
Furthermore, we want to better understand how an OSE can, in the longer term, support and sustain such efforts.

<!--
### `YAGLM`
-->

###

The `YAGLM` open-source Python package was developed to make the framework of modern GLM methodology (various loss function, regularizer, solvers) available and easily accessible to data analysts \cite{carmichael2021yaglm}.
Beyond the basic lasso/ridge, the package supports structured penalties such as the nuclear norm as well as the group, exclusive, fused, and generalized lasso and non-convex penalties.
`YAGLM` comes with a variety of tuning parameter selection methods including: cross-validation, information criteria that have favorable model selection properties, and degrees of freedom estimators.

Standard statistical software design patterns had to be rethought in order to handle the breadth of the GLM framework.
For example, scikit-learn’s API and estimator object backend \cite{sklearn_api} have
become a frequently used template for developing statistical and
machine learning software \cite{pmlr-v80-massias18a}. Initial attempts at extending scikit-learn quickly
revealed that different backend and frontend API design choices will need
to be made. Some of these design choices (e.g., configuration objects to
specify models or a separate solver object class for the optimization
algorithm) will be impactful for other statistical software packages.

The initial development of `YAGLM` was done in short bursts by a few
core developers. It is currently available on GitHub and has some
users. `YAGLM` is missing important engineering details like continuous
integration, extensive testing, and quality documentation. It is also
missing community support like governance, developer onboarding and a
code of conduct.

<!--
### ISLP
-->

###

The `ISLP` open-source Python package is written to accompany an introductory text on statistical learning and Python (*An Introduction to Statistical Learning: with Applications in Python* \cite{james2023introduction}),
closely following the examples in its hugely successful `R` version. Besides just providing labs,
it provides Pythonic design matrix building, a simple implementation of Bayesian Additive Regression Trees
and object oriented stepwise model selection. Planned development include extending the `pygam` package,
regularized regression specification (to be used by `YAGLM`), and integration of a Python version
of the very popular `glmnet` package in `R`.

The corresponding textbook was published in July.  The project aims to
use good (if not best) software engineering practices.  It is expected
that it will be used in several introductory data science and
statistics courses nationwide which will serve to test the robustness
of these practices, evidenced by the responsiveness to (GitHub) and other issues that arise.

## Guiding Principles and Long Term Vision

As described above, the current state of open source statistical software is mixed. The `R` community has many individual or small group contributors, though many lack proper training in best practices for open source software.
In the Python community, at least as represented by the larger packages, is represented by larger, well-organized groups with clear governance practices.

This proposal aims to bridge these two worlds: it is unreasonable to assume statisticians trained in cutting-edge methodology to simultaneously master best practices in software engineering.
Similarly, software engineers are not trained at the cutting edge of statistical methodology.
However, there is certainly a middle ground: graduate students in statistics can be trained in good (i.e. not as extensively as required
for "best") practices in software engineering.
Similarly, those with strong software engineering skills can learn what are the types of APIs required to implement cutting edge methodology in software.

Bridging these worlds achieves several goals:

1. Better software engineering practices for academically trained statisticians writing software both in `R` and Python.

2. Establishment of new, well-engineered and robust APIs (building on the
success of `sklearn`'s simple but powerful API \cite{sklearn_api}) for implementation of cutting-edge statistical
methodology in different modeling paradigms.

3. Cross-pollination between `R` and Python statistical software communities. The current state sees
`R` with mostly small development groups with Python leaning toward larger groups. Meeting in this middle
ground will necessitate communication between the groups.

## Societal Needs and Broader Impact

Statistics software are a fundamental component to almost any research software stack.
This work disseminates best software engineering practices to both the R and Python ecosystems.
It brings the methods expertise of statisticians to research software development, while providing statisticians with the capability to improve the quality of software they develop.
The OSE distills knowledge on how to transform experimental research products into robust, high-quality research software into a centralized resource; that resource, in turn, is then used to transform other research products.
By hosting fundamental educational resources on both statistical techniques and software development best practices, the OSE builds pathways that onboard academics to statistical scientific software development.
This empowers young researchers, and increases participation both in research and research software development.

# Team

Our team is well established in the statistics and scientific Python
communities. We are uniquely positioned for creating a community around a Statistical Python OSE:\

**Stéfan van der Walt** is a research scientist at UC Berkeley. He is the founder of scikit-image and co-author of Elegant SciPy.
He contributes to numerous packages in the ecosystem including NumPy, SciPy, scikit-image, and NetworkX.
Stéfan is a director of NumFOCUS, and serves on the steering committees of NumPy, SciPy, and the PSF's Scientific Working Group.
He cofounded the Scientific Python project.

**Jarrod Millman** is a senior developer at UC
Berkeley. He cofounded the Neuroimaging in Python project.
He was the NumPy and SciPy release manager from 2007 to 2009
and the SciPy steering committee from
2007 to 2010.
He cofounded NumFOCUS and
served on its board from 2011 to 2015.
He is the release manager of NetworkX, scikit-image, pygraphviz, numpydoc, and other packages.
He cofounded the Scientific Python project.

**Iain Carmichael** is a visiting assistant professor of statistics at UC Berkeley.
His research focuses on developing statistical/machine learning algorithms for data with a complex structure such as networks, images, and multi-view/modal data.
He wrote `YAGLM`.

**Jonathan Taylor** is a professor of statistics at Stanford University. His
research focuses on selective inference and signal detection in structured
noise. He has been involved in the scientific Python community for many years
and works closely with statisticians in the `R` community.
He cofounded the Neuroimaging in Python project.
In collaboration with Trevor Hastie, he is the main developer on `ISLP` a package bridging the `R` and
Python worlds by providing Python support for course material in the
hugely successful *An Introduction to Statistical Learning: with
Applications in R* \cite{james2013introduction}.

# Program of Work

<!--
- Set up OSE that it works in SP ecosystem with domain-specific OSEs
- Guiding principle: learn how existing domain-specific OSEs work, and distill best practices into a blueprint
- Incorporate the strengths and best practices of R ecosystems like Bioconductor and tidyverse
- Use principles derived from the above and pilot projects, to learn how to best support other projects and developers as the ecosystem grows

* Community based governance
  * Scientific Python-style governance
* Mimic orgs like scipy-hep, pangeo, astropy other domain-specific OSEs, a stack for statistics (Bioconductor)
-->

We will undertake scoping activity for a
Statistical Python OSE formed around our two pilot projects in the preparation
of a Phase II proposal that will aim to build a sustainable and robust ecosystem. 
The main deliverable for the current proposal will be the creation of a
detailed plan documenting the need for the innovation within the current
technological landscape, explaining why an OSE is the right approach,
outlining methods to identify potential contributors and users,
and specifying the Statistical Python OSE infrastructure, organization,
governance, and long-term sustainability.

<!--
Include a plan for developing a strategy that: (1) describes methods to
evaluate and justify the need for the innovation within the current
technological landscape; (2) explains why an OSE is the right approach to
further develop the technology; and (3) outlines methods to identify potential
users who will utilize this technology.
-->

## Activities

The activities that will craft this plan includes auditing the two pilot
projects, understanding how related OSEs work, and gathering feedback from the
statistical community through surveys, informal meetings, and two-day workshops.\

**Pilot Project Audits.**
We will perform detailed code and governance audits on `YAGLM` and `ISLP`.
The goal of these audits is to better understand what type of training, technical & social infrastructure,
and software development practices these projects need to become rigorous and
sustainable open source projects like many existing projects in the scientific
Python ecosystem.

**Engagement with Related OSEs.**
We will engage community members and leaders of existing Scientific Python
domain-specific OSEs as well as of Bioconductor and Tidyverse.
We will determine what social and technical structures they deem important,
and which deficiencies they'd like to see addressed.
We will inquire about the history of those projects, and determine
lessons learned that may benefit the design of the Statistical Python
OSE.

**Ecosystem Discovery.**
At the start of the funding cycle, we will create and widely-circulate
surveys---targeted at students, teachers, and researchers---to better
understand the statistics community's interest and need for a Statistical
Python OSE.
We will also engage our colleagues in informal gatherings or Birds of a Feather sessions (BOFs)
at community meetings such as SciPy, EuroSciPy, Joint Statistical Meetings, and other meetings
that the senior personnel attend.

We will also organize four workshops.

- **Workshop 1 & 2** (targeting `YAGLM` & `ISLP`) will focus on each project's current technical landscape, and identify ways of
maturing the project and facilitating broader adoption. Participants will include community members (users and developers),
experts in generalized linear models and statistical learning, as well as teachers.
 This discussion will also identify potential new users and contributors.

- **Workshop 3** will focus on statisticians working in Python. We will identify, through the previous meetings and a survey, statisticians who have developed additional open-source products that may benefit from a Statistical Python OSE.

- **Workshop 4** will focus on a plan for developing the Phase II proposal including identifying specific resources needed to create a sustainable infrastructure for the Statistical Python OSE.

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

We will leverage our experience of establishing and growing the Scientific
Python OSE, the NIPY OSE, various successful open-source projects such as
scikit-learn and NetworkX, as well as the non-profit organization NumFOCUS.
In addition, we will actively engage with other active domain-specific OSEs in
the Python ecosystem to learn which modern practices they have adopted that
significantly contribute to the success of their platforms.

## Community Building

<!--
Describe the specific activities to engage potential users and intellectual
content developers, including: (1) identification of the specific research and
development capabilities required of the potential contributor communities; and
(2) mechanisms to engage these communities (e.g., workshops, hackathons,
competitions, research coordination networks, and Ideas Labs).
-->

Workshop discussions will focus significant attention on community building for
the Statistical Python OSE. The scoping activities will also include
involvement in community engagement activities.
We will utilize our existing connections, and platforms created for, Scientific
Python to engage that community, who very likely have shared interests, and ask
them to help us introduce statisticians, developers, and potential users in the
project.



# Intellectual Merit

<!--
The Intellectual Merit criterion encompasses the potential to advance knowledge;
-->

This proposal addresses two gaps in the statistical software ecosystem. On the one hand,
there  are many small groups or individual developers of statistical packages who lack the training
in best (or better) practices in software engineering needed for open source an project to survive. On the other hand,
the scientific Python community adheres closely to such standards, resulting in well-engineered software
packages such as NumPy, SciPy, pandas, and scikit-learn. This proposal seeks to
learn and document how to bridge this gap, starting with `YAGLM` and `ISLP` as pilot
projects. From this knowledge, the OSE will be able to derive and propagate
models of best practices, resulting in better engineered software in the
statistical community, as well improved software development skills among
statisticians.

The context of statistical software today is such that the `R` developer community, which are responsible for many of the innovative statistical implementations, consists of many
individual or small groups, while scientific Python core projects and domain stacks tend to be larger projects that operate on a scale and have resources to apply modern software engineering practices. Building small, exploratory packages that are also well-engineered will necessitate
a bridge between the `R` and scientific Python communities. Learning what works best in each development community,
uncovering the common ground that exists between them, and communicating those concepts, will form the foundation of this bridge.

# Broader Impacts

The broader impacts of this proposal are in establishing
better software engineering practices in the  statistical community.
This will result in better onboarding pathways to involve young researchers,
healthier and more inclusive community practices and resources that can be applied to other projects and fields.
In addition, this is expected to result in more statistical libraries available to researchers using Python
as well as a cross pollination of best practices between `R` and Python.

<!--
The Broader Impacts criterion encompasses the potential to benefit society and
contribute to the achievement of specific, desired societal outcomes.
-->

<!--
Broader impacts may be accomplished through the research itself, through the activities that are directly related to specific research projects, or through activities that are supported by, but are complementary to, the project. NSF values the advancement of scientific knowledge and activities that contribute to achievement of societally relevant outcomes. Such outcomes include, but are not limited to: full participation of women, persons with disabilities, and other underrepresented groups in science, technology, engineering, and mathematics (STEM); improved STEM education and educator development at any level; increased public scientific literacy and public engagement with science and technology; improved well-being of individuals in society; development of a diverse, globally competitive STEM workforce; increased partnerships between academia, industry, and others; improved national security; increased economic competitiveness of the United States; and enhanced infrastructure for research and education.
-->

# Results from Prior NSF Support

<!--
The purpose of this section is to assist reviewers in assessing the quality of prior work conducted with prior or current NSF funding. If any PI or co-PI identified on the proposal has received prior NSF support including:

    an award with an end date in the past five years; or

    any current funding, including any no cost extensions,

information on the award is required for each PI and co-PI, regardless of whether the support was directly related to the proposal or not. In cases where the PI or any co-PI has received more than one award (excluding amendments to existing awards), they need only report on the one award that is most closely related to the proposal. Support means salary support, as well as any other funding awarded by NSF, including research, Graduate Research Fellowship, Major Research Instrumentation, conference, equipment, travel, and center awards, etc.

The following information must be provided:

(a) the NSF award number, amount and period of support;

(b) the title of the project;

(c) a summary of the results of the completed work, including accomplishments, supported by the award. The results must be separately described under two distinct headings: Intellectual Merit and Broader Impacts;

(d) a listing of the publications resulting from the NSF award (a complete bibliographic citation for each publication must be provided either in this section or in the References Cited section of the proposal); if none, state “No publications were produced under this award.”

(e) evidence of research products and their availability, including, but not limited to: data, publications, samples, physical collections, software, and models, as described in any Data Management Plan; and

(f) if the proposal is for renewed support, a description of the relation of the completed work to the proposed work.

If the project was recently awarded and therefore no new results exist, describe the major goals and broader impacts of the project. Note that the proposal may contain up to five pages to describe the results. Results may be summarized in fewer than five pages, which will give the balance of the 15 pages for the Project Description.
-->

SJvdW is co-PI on NSF Award #2206744 in the amount of $572,926.00 to the University of California, Berkeley.
As an unfunded member of the collaboration, he advises on the development of the `nbi` software package.
The project has produced several publications \cite{nbi0, nbi1, nbi2, nbi3}.
**Intellectual Merit:** Accelerate model-based inference across NSF-supported science. The proposed software allows likelihood-free inference as a drop-in replacement for traditional sampling-based approaches across a wide range of domains.
**Broader Impacts:** Bring together a diverse group of participants around likelihood-free inference. Provide open-source lecture materials to improve STEM education and research requiring computationally expensive forward models. Reduce the cost of inference by orders of magnitude, thereby lowering carbon footprints.

<!-- Iain's award: https://www.nsf.gov/awardsearch/showAward?AWD_ID=1902440&HistoricalAwards=false -->

IC was awarded an NSF PostDoctoral Research Fellowship #1902440 ("Modeling, integration, and analysis of complex, hierarchical, and multi-view data") of $150,000 from
July 1, 2019 to June 30, 2023. 
The project has produced several publications \cite{carmichael2021yaglm, carmichael2021joint, carmichael2020learning, perry2021mvlearn, carmichael2021folded, carmichael2021geometric, gazzola2023s, gazzola2022cohort}.
**Intellectual Merit:** The development of the `YAGLM` package required the
development of improved statistical software design patterns and summarizing
the modern state of the art of
generalized model statistical and optimization methodology into a coherent
framework.
This work provided both computational and statistical guarantees for algorithms that involved
non-convex optimization procedures as well as the development of new
modeling tools (e.g. the folded concave Laplacian penalty).
**Broader Impacts:** The `YAGLM` package has significant potential to impact
all fields of science because generalized linear models are widely used
statistical tools. Few of the modern statistical or optimization
tools are actually available to data scientists and `YAGLM` is a big step
forward in making these advanced tools broadly available.
Multi-view clustering models may lead to better scientific understanding in
domains where multi-view data are studied such as
cancer genetics and neuroscience.
Work on the folded concave Laplacian
penalty may help people with network structured model parameters better
understand their complex models.


<!--

Phase I proposals will be evaluated on the basis of the following solicitation-specific review criteria:

- Does the proposal present a convincing case that the OSE will address an issue of significant societal or national importance that is not currently being adequately addressed?
- Does the proposal clearly describe the long-term vision for the OSE, including potential partnerships and sustainability?
- Does the proposal provide convincing evidence that a substantial user base exists, or could be built, for the open-source product that will be the subject of the OSE?
- Does the proposal justify the OSE within the current technological landscape and present a strong case that an OSE is the best approach for generating impact?
- Does the proposal present clear plans for discovering the ecosystem within which the OSE will be operating?
- Does the proposal present a credible plan for exploring the establishment of a sustainable organizational structure?
- Does the proposal present a credible plan to develop a strategy for building a community of contributors?
- Will NSF support serve as a critical catalyst for the establishment of the OSE?


- Does the proposing team have the required expertise and experience to undertake the Phase I activities described in the solicitation?
- Does the proposal include third-party letters of collaboration from current users of the open-source product that is the subject of the OSE?

-->
