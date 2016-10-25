def largest_product(seq_d, n):

    def _seq_product(substring):
        _num = [int(c) for c in substring]
        return reduce(lambda x,y:x*y, _num)

    # assert len(seq_d) < n, 'The digit sequence should be larger than the substring length.'


    max_prod = 1
    if n > 0 and seq_d:
        if not seq_d.isdigit():
            raise ValueError('Invalid character')

        max_prod = _seq_product(seq_d[0:n])
        for x in xrange(len(seq_d)-n):
            current_product = _seq_product(seq_d[x:x+n])
            if current_product > max_prod :
                max_prod = current_product
    elif n < 0:
        raise ValueError('Negative Span')

    return max_prod
