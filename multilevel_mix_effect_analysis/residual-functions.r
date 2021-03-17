# residuals...

r.marg <- function(m) {
  y <- m@frame[,1]
  yhat <- model.matrix(m) %*% fixef(m)
  return(y-yhat)
}

r.cond <- function(m) {residuals(m)}

r.reff <- function(m) {r.marg(m) - r.cond(m)}

Sigma.y <- function(m) {
    rel.var.eta <- crossprod(getME(m,"Lambdat"))
    Zt <- getME(m,"Zt")
    var.epsilon <- sigma(m)^2

    var.eta <- var.epsilon*(t(Zt) %*% rel.var.eta %*% Zt)
    sI <- var.epsilon * Diagonal(length(getME(m,"y")))
    var.y <- var.eta + sI

    return(var.y)
}


r.chol <- function(m) {

    var.y <- Sigma.y(m)

    S <- chol(var.y)

    resid.chol <- (solve(t(S))%*%r.marg(m))@x

    return(resid.chol)
}

r.stnd <- function(m) {

    var.y <- Sigma.y(m)

    SDs <- diag(sqrt(diag(var.y)))

    resid.stnd <- solve(SDs)%*%r.marg(m)

    return(resid.stnd)
}


# suitable fitted values to plot them against...
# (you can plot them against other things as well...

yhat.marg <- function(m) { model.matrix(m) %*% fixef(m) }

yhat.cond <- function(m) {
  y <- m@frame[,1]
  y - r.cond(m)
}

yhat.reff <- function(m) { yhat.marg(m) + r.cond(m) }

