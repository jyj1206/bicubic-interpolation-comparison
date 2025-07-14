function [out, elapsed] = matlab_bicubic(img, factor)
    tic;
    out = imresize(img, factor, 'bicubic');
    elapsed = toc;
end
