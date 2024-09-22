# Overview
This repository contains assorted programs and functions for using numerical methods, modeling, and solving common problems in systems biology. 

# Numerical Methods

Numerical methods are techniques for finding approximate solutions to mathematicaal problems that may not have exact solutions. Additionally, numerical methods generally rely on iterative precedures and discretization to produce a sequence of approximations that converge to a true solution, and as a result they are  particuarly helpful for solving differential equations, optimization problems, and systems of equations where traditional algebraic methods are not possible, or are impractical. 

Below you'll find a list of numerical methods for which I've provided functions to carry out. Additional numerical methods will be added to this repository over time.

- [Euler's Method](https://github.com/evanpeikon/numerical-methods/blob/main/eulers_method.py)
  - Euler's method is a simple numerical technique for solving ordinary differential equations (ODEs) and works by approximating the solution over small steps.
- [Runge-Kutta 4th Order Method (RK4)](https://github.com/evanpeikon/numerical-methods/blob/main/runge_kutta_RK4.py)
  - The RK4 method is a more accurate method for solving ODEs compared to Euler's method. RK4 reduces error by taking a weighted average of slopes at different points within the interval, and it's known for it's balance between accuracy and computational efficiency.
 - Root Finding Methods:
   - The quadratic formula $x = \frac{-b±\sqrt{b^2-4ac}}{2a}$ is used to solve functions of the form $f(x) = ax^2+bx+c=0$. The values calculated with this formula are called ```roots``` and they represent values of $x$ that make the function equal 0. Although the quadratic formula helps you identify roots for simple functions of the form $f(x) = ax^2+bx+c=0$. there are many functions for which the root cannot be determined as easily. For this reason, other numerical methods, provide more effcient means of obtaining the answer(s). Below you'll find code for multiple bracketing and open methods used to identify roots: 
    - [The Bisection Method](https://github.com/evanpeikon/systems_biology/blob/main/bisection_method.py)
    - [The False Position Method](https://github.com/evanpeikon/systems_biology/blob/main/false_positon_method.py)
 
# Systems Biology

Below you'll find a list of programs and functions for solving common problems in systems biology. Additional methods will be added to this repository over time.

- [Binomial Mutations Calculator](https://github.com/evanpeikon/numerical_methods_and_systems_bio/blob/main/binomial_mutation_calculator.py)
  - A binomial process is related to the binomial distribution, which describes the number of successes in a fixed number of independent trials, each with the same probability of success. This code calculates the probability of observing exactly k mutations in n DNA bases, given a mutation rate p, using the binomial distribution formula. 
- [Poisson Mutation Calculator](https://github.com/evanpeikon/numerical_methods_and_systems_bio/blob/main/poisson_mutation_calculator.py)
  - A Poisson process is related to the Poisson distribution, which describes the number of events occurring within a fixed interval of time or space, where these events happen independently of each other and at a constant average rate. This code calculates the probability of observing exactly k mutations given an average mutation rate λ, using the Poisson distribution formula. 
- [Dynamical System Modeling](https://github.com/evanpeikon/systems_biology/blob/main/dynamical_system_modeling.py)
  - A dynamical system is a framework used to understand and predict how the behavior of complex systems evolve and change over time. At its core, a dynamical system consists of a finite set of variables, each representing a quantity of interest, and a predefined set of rules that govern how these variables change over time. By defining a set of variables and their evolutionary rules, we can capture the essence of dynamic phenomena and gain insights into their future states, which can be used to model a wide range of systems. For example, in biology dynamical systems may be used to model population dynamics, disease spread, and interactions between specifies, while in economics they may be used to represent market dynamics, the evolution of stock prices, and the behavior of economic indicators.
- [Markov Chains](https://github.com/evanpeikon/systems_biology/blob/main/markov_chain.py)
  - A Markov chain is a type of dynamical system where the exact state of the variables isn't known for sure, so they are expressed as probabilities. These systems are called stochastic processes because their future states depend on both predictable factors and inherent randomness.

