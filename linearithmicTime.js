function closestPair(a, cd) {
    let mf = function(a) {
        a = a.slice();
        if (a.length < 2) return [9999999, 0, 0];
        if (a.length == 2) return [cd(a[0], a[1]), a[0], a[1]];

        var q = Math.floor(a.length / 2);
        var a1 = a.slice(0, q);
        var a2 = a.slice(q);
        var [mi1, x1, y1] = mf(a1);
        var [mi2, x2, y2] = mf(a2);
        if (mi1 < mi2) {
            var [mi, x, y] = [mi1, x1, y1];
        } else {
            var [mi, x, y] = [mi2, x2, y2];
        }
        var b = a.filter(p => Math.abs(p[0] - a[q][0]) < mi);
        b.sort((a, b) => a[1] - b[1]);
        for (let i = 0; i < b.length - 1; i++) {
            for (let j = i + 1; j < b.length; j++) {
                if (b[j][1] - b[i][1] > mi) break;
                var mid = cd(b[i], b[j]);
                if (mid < mi) {
                    var [mi, x, y] = [mid, b[i], b[j]];
                }
            }
        }
        return [mi, x, y];
    }

    a = a.slice();
    a.sort((a, b) => a[0] - b[0]);

    var [_, x, y] = mf(a);

    return [x, y];
}

//https://www.codewars.com/kata/5376b901424ed4f8c20002b7/train/python