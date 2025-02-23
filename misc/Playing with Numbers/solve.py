import numpy as np

def rot_encode(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)

def rotate(strg, n):
    return strg[n:] + strg[:n]

# encoding = np.array([[-3, -3, -4], [0, 1, 1], [4, 3, 4]])

# message = np.array(
#     [
#         [16, 16, 5, 15, 6, 20, 20],
#         [18, 1, 27, 27, 7, 9, 5],
#         [5, 18, 20, 14, 15, 1, 27],
#     ]
# )

# encoded = np.matmul(encoding, message)

# decoding_matrix = np.linalg.inv(encoding)

# decoded_message = np.matmul(decoding_matrix, encoded)

# print(decoded_message)

# encoded = [
#     [180, 487, 279, 404, 282, 148, 494],
#     [4, -104, -50, -18, -110, -20, -70],
#     [263, 418, 272, 511, 131, 154, 512],
# ]

# decoding = [
#     [-12 / 5, -41 / 10, 9 / 5],
#     [23 / 15, 79 / 30, -16 / 15],
#     [-8 / 5, -29 / 10, 6 / 5],
# ]


encoded = np.array([[2, 4, -1], [3, -6, 1], [8, 4, -1]]).T

decoding = np.array(
    [
        [
            -103.08333333,
            -131.25,
            -81.41666667,
            -91.58333333,
            -25.25,
            -63.5,
            -60.33333333,
            -12.75,
            -151.08333333,
        ],
        [-40.5, -52.5, -34.5, -36.5, -10.5, -28.0, -25.0, -4.5, -62.5],
        [
            42.58333333,
            54.75,
            34.91666667,
            39.08333333,
            11.75,
            26.5,
            26.33333333,
            7.25,
            63.58333333,
        ],
    ]
)


res = np.matmul( encoded, decoding)

# print(res)
# print(res.T)

out = np.ndarray.flatten(res.T)

# print(out)

# for i in range(26):
alpha = rotate("abcdefghijklmnopqrstuvwxyz", 0) + "_"

for char in out:
    print(alpha[round(char - 1)], end="")
print()
# print(out)
# matrixmultiplicationiseasyy