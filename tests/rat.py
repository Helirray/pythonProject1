import math


def make(num, den):
    n = int(num / math.gcd(num, den))
    d = int(den / math.gcd(num, den))
    return {'numer': n, 'denom': d }


def get_numer(rat):
    return rat['numer']


def get_denom(rat):
    return rat['denom']


def compute_lcm(den1, den2):
    lcm = (den1*den2) / math.gcd(den1, den2)
    return lcm


def common_denum(rat1, rat2):
    num1 = get_numer(rat1)
    num2 = get_numer(rat2)
    den1 = get_denom(rat1)
    den2 = get_denom(rat2)
    lcm = compute_lcm(den1, den2)
    mul1 = int(lcm / den1)
    mul2 = int(lcm / den2)
    num1 = mul1 * num1
    den1 = mul1 * den1
    num2 = mul2 * num2
    return {'numer': num1,'denom': den1}, {'numer': num2, 'denom': den1}


def add(rat1, rat2):
    r1, r2 = common_denum(rat1, rat2)
    return make(get_numer(r1) + get_numer(r2), get_denom(r1))


def sub(rat1, rat2):
    r1, r2 = common_denum(rat1, rat2)
    return make(get_numer(r1) - get_numer(r2), get_denom(r1))


def make(numer, denom):
    gcd = math.gcd(numer, denom)
    return {
        "numer": int(numer / gcd),
        "denom": int(denom / gcd),
    }


def get_numer(rat):
    return rat["numer"]


def get_denom(rat):
    return rat["denom"]


def add(rat1, rat2):
    numer1 = get_numer(rat1)
    denom1 = get_denom(rat1)
    numer2 = get_numer(rat2)
    denom2 = get_denom(rat2)

    return make(
        numer1 * denom2 + numer2 * denom1,
        denom1 * denom2,
    )


def sub(rat1, rat2):
    numer1 = get_numer(rat1)
    denom1 = get_denom(rat1)
    numer2 = get_numer(rat2)
    denom2 = get_denom(rat2)

    return make(
        numer1 * denom2 - numer2 * denom1,
        denom1 * denom2,
    )


rat11 = make(3, 9)
rat3 = make(-4, 16)
rat4 = make(12, 5)
rat5 = add(rat3, rat4)
print(get_numer(rat5))
print(get_denom(rat5))